from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def booking(request):
    return render(request, 'booking.html')
# Serializer - MenuItemSerializer
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
class SingleMenuItemVIew(generics.RetrieveUpdateAPIView,
                         generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
# Serializer - BookingSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            return redirect('restaurant:booking_confirmation', booking_id=booking.id)  # Redirect to confirmation page
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def booking_confirmation_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)  # Retrieve booking from DB
    return render(request, 'booking_confirmation.html', {'booking': booking})

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # only authenticated users can access