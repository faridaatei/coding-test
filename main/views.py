from django.shortcuts import render


# Create your views here.
def home(request):
    # return render(request, 'main/index.html')
     return render(request, 'chart.html')

     

# def register():
#     data = dict(request.form.measurements()
#     if data.get('amount of rainfall', None):
#         form.create(
#             amount of rainfall=data.get('measurements', 'mm'),
            
           
            
            
#         )
    # return render_template("jsonify")



