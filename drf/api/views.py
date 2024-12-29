from rest_framework import viewsets
from .models import Artista, Album, Musica
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Artistas
    """

    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class MusicaViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """

    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
