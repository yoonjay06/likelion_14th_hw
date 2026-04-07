from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'html': 'templates폴더 안에 메인페이지 생성',
            'views': 'views.py 작성 후 메인페이지 렌더링',
            'secondpg': 'secondpage도 동일하게 진행'
        },
        'shortcuts': [
            'HTML 링크 연결 : secondpage를 누르면 해당페이지로 넘어가게 설정',
            '변수 사용 : 변수 -> {{변수}}, 변수의 속성 -> {{변수.속성}}, list의 각 index -> {{list.값의 위치}}, dict의 value값 -> {{dict.key}} ',
            '반복문 : for문 사용 예시 -> {% for product in products %} <p>{{product.name}}</p> {% endfor %}',
            '조건문 : if문 사용 예시 -> {% if 조건 %} 참이네요! {% else %} 거짓이네요! {% endif %} ',
            'Template 필터 : 필터는 주로 변수와 함께 쓰이며 원하는 형태로 값을 변환하기 위해 사용한다.',               
        ]
    }
    return render(request, 'main/mainpage.html', context)
def secondpage(request):
    return render(request, 'main/secondpage.html')