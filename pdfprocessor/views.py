import fitz  # PyMuPDF
import nltk
from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import DocumentAnalysis
from .serializers import DocumentAnalysisSerializer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")


class DocumentAnalysisView(views.APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "PDF file required."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Extract text from PDF
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        # Process text to find nouns and verbs
        tokens = word_tokenize(text)
        tagged_tokens = pos_tag(tokens)
        nouns = ", ".join([word for word, tag in tagged_tokens if tag.startswith("NN")])
        verbs = ", ".join([word for word, tag in tagged_tokens if tag.startswith("VB")])

        # Save to database
        serializer = DocumentAnalysisSerializer(
            data={
                "email": request.data.get("email"),
                "content": text,
                "nouns": nouns,
                "verbs": verbs,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, "index.html")
