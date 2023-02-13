
from .models import Job
from .serializers import Jobserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def joblistapi(request):
    jobs = Job.objects.all()
    serializer = Jobserializer(jobs, many=True)
    return Response(serializer.data)