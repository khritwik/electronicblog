from rest_framework import serializers
from blog.models import Article

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = ('id','image','image2','title','slug','author','text','text2','quote','quote_name','l_heading','l_heading_text','s_heading','s_heading_text','category','created_date','tag_1','tag_2','tag_3',)