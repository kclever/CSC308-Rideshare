from rest_framework import serializers

from api.models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'name_u', 'from_u', 'to_u', 'when_u', 'seats_u', 'cost_u', 'will_drop_u', 'extra_details_u')
		# fields = ('id', 'Name', 'From', 'To', 'When')
		# fields = ('id', 'Title', 'Description')