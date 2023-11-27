
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, authentication
from twilio.twiml.messaging_response import MessagingResponse
from .serializers import SmsSerializer
from .models import SmsInfo


class TwilioWebhookView(APIView):

    def post(self, request):
        # Validar os dados recebidos da Twilio
        try:
            message_body = request.data['Body']
            sender = request.data['From']
            recipient = request.data['To']
        except KeyError as chave_json:
            return Response({'detail': f'Campo obrigatório ausente: {chave_json}'}, status=status.HTTP_400_BAD_REQUEST)

        # Validar  os dados de acordo com as regras que coloquei no serializer, nesse caso nenhuma, o papel do serializer vai ser pegar os dados recebidos por http, e salvar no banco de dados com o serializer.save()
        serializer = SmsSerializer(data={
            'message': message_body,
            'sender': sender,
            'recipient': recipient
        })

        if serializer.is_valid():
            serializer.save()

            # Enviar uma resposta de confirmação para a Twilio
            response = MessagingResponse()
            response.message("Mensagem recebida com sucesso!")
            return Response(str(response))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SmsInfoListView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = SmsSerializer(SmsInfo.objects.all(), many=True)
        return Response(serializer.data)