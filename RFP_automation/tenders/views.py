from django.shortcuts import render, get_object_or_404
from .models import Tender
from services.llm_service import analyze_tender_with_llm, generate_response_with_llm

def recommend_tender(request):
    if request.method == 'POST':
        tender = Tender.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            document=request.FILES.get('document')
        )
        analysis = analyze_tender_with_llm(tender.description)
        tender.recommendation_score = analysis.get('score', 0.0)
        tender.save()
        return render(request, 'tenders/recommend.html', {'tender': tender, 'analysis': analysis})
    return render(request, 'tenders/recommend.html')

def generate_response(request, tender_id):
    tender = get_object_or_404(Tender, pk=tender_id)
    if not tender.generated_response:
        tender.generated_response = generate_response_with_llm(tender.description)
        tender.save()
    return render(request, 'tenders/generate_response.html', {'tender': tender})
