import requests
from bs4 import BeautifulSoup
import pandas as pd

#num은 크롤링한 자동차 index를 붙이기 위해 만든다.
#num을 초기화한다.
num = 0

#자동차 정보를 모으기 위해 만든다.
#car를 초기화한다.
car = []

#위에서 만든 자동차 정보를 리스트로 만든다.
#carlist 초기화 한다.
carlist = []

#range(1,184)는 자동차 페이지의 수가 약 184개쯤 되기 때문에 설정함
#for를 돌리는 이유는 자동차사이트페이지마다 모두 크롤링 하기 위함
for k in range(1,184):

    #네이버 자동차 검색 사이트
    #source맨 끝에 k가 있음. 이것은 페이지마다 크롤링하기 위해 넣어것.
    source = requests.get(
        "https://auto.naver.com/search/detailSearch.nhn?kor_all=true&kor=16&kor=12&kor=13&kor=15&kor=61321&kor=14&kor=124773&kor=4057&kor=53301&kor=123175&kor=138293&glo_all=true&glo=23&glo=39&glo=35&glo=3976&glo=6435&glo=21&glo=24&glo=48&glo=3848&glo=18&glo=25&glo=40&glo=19&glo=26&glo=30&glo=3905&glo=20&glo=28&glo=68669&glo=60005&glo=130511&glo=59315&glo=128687&glo=29611&glo=133879&glo=29981&glo=61803&glo=137057&glo=52403&glo=60307&glo=54155&glo=121227&glo=33&glo=29972&glo=47943&glo=4188&glo=53987&glo=121261&glo=56237&glo=29975&glo=3814&glo=64245&glo=120951&glo=58801&glo=22&glo=29985&glo=4040&glo=3824&glo=68685&glo=3847&glo=137215&glo=128425&glo=68379&glo=40077&glo=68723&glo=6434&glo=53655&glo=42&glo=29977&glo=29978&glo=44&glo=29979&glo=37&glo=50851&glo=30042&glo=55877&glo=133923&glo=58887&glo=4129&glo=124709&glo=29989&glo=134383&glo=58745&glo=67995&glo=43&glo=29&glo=4216&glo=29982&glo=46&glo=29984&glo=30040&glo=6436&glo=47&glo=45&glo=3801&glo=29987&glo=29970&glo=54257&glo=135009&glo=3999&glo=29971&glo=3827&glo=32&glo=133877&glo=55563&glo=53657&glo=54157&glo=29391&glo=68661&glo=29974&glo=34&glo=19376&glo=61293&glo=29973&glo=18001&glo=49801&glo=3840&glo=55571&glo=140349&glo=29988&glo=29832&glo=41&glo=3806&glo=68693&glo=27&glo=50823&glo=60645&glo=36&glo=129857&glo=126821&glo=4029&glo=3990&glo=30039&glo=31&glo=3785&glo=63395&kind_all=true&kind=0&kind=1&kind=2&kind=3&kind=4&kind=5&look_all=true&look=0&look=1&look=2&look=3&look=4&look=5&look=6&look=7&look=8&superCar=true&fuel_all=true&fuel_dsl=Y&fuel_gas=Y&fuel_lpg=Y&fuel_hbrd=Y&fuel_eltr=Y&fuel_hydg=Y&lwst_prc=&hiest_prc=&lwst_dsplc=&hiest_dsplc=&lwst_flef=&hiest_flef=&lwst_hspw=&hiest_hspw=&market=1&page="+str(k)).text
    soup = BeautifulSoup(source, "html.parser")

    # 네이버 자동차 검색사이트 태그
    name = soup.select("dt.name")
    employee = soup.select(".etc a")
    empty = soup.select(".new.etc")
    va = soup.select(".detail_list input.chk")
    img = soup.select(".thumb img")

    #enumerate()는 for가 돌아갈때 index를 가져오기 위해.
    #index= index, key = 자동차의 정보?
    for index,key in enumerate(name):

        #detail은 자동차 상세 정보를 모아두기 위해 만든다.
        detail = []

        #num은 자동차 리스트에 index를 붙이기 위함
        num += 1

        #carid는 네이버자동차 사이트에서 각 자동차마다 고유로 붙여있는 id를 가져오기 위함
        # 네이버에서 제공하는 자동차id를 활용하여 자동차detail 페이지의 정보를 가져온다.
        carid = va[index]['value']

        # 네이버 자동차 디테일 사이트
        # 자동차 디테일 페이지를 들어가기 위함
        source1 = requests.get("https://auto.naver.com/car/lineup.nhn?yearsId=" + str(carid)).text
        soup1 = BeautifulSoup(source1, "html.parser")

        # 네이버 자동차 디테일 사이트 태그
        carDetail = soup1.select(".lineup_btm_td li")

        #for를 돌리는 이유는 자동차 디테일 사이트에 있는 35개의 리스트를 가져오기 위함
        #try: excpt: 는 "indexerror: list index out of range" 오류로 부터 빠져나와 진행할 수 있도록하기 위한 예외처리
        for i in range(0,40):
            try:
                #선택된 페이지의 정보를 detail에 넣어둔다.
                #.replace('바꿀문자','대체되는 문자')는 지정된 문자를 다른 문자로 바꾸기 위함
                detail.insert(i, carDetail[i].text.replace("\r", "").replace("\n", "").replace(" ", "").replace("\xa0","").replace(",",""))
            except:
                break

        #자동차 정보를 저장한다.
        car = (str(num)+"," + name[index].text.replace("\n","") + "," + employee[index].text.replace("\n","") + "," +empty[index].text.replace("\n","").replace(",","")+ ","+",".join(detail)+","+img[index]['src']).split(",")

        #저장한 자동차 정보를 carList에 담는다.
        carlist.insert(num,car)
        print(car)
        print("--------------------------")

print("---------------종합---------------------")
print(carlist)

#csv에 저장한다.
data = pd.DataFrame(carlist)
#csv파일을 생성하고 이름은 지정한다. index=False은 csv저장시 자동으로 index가 붙는 것을 막는다. encoding='cp949'은 인코딩 방식이다. (UTF-8은 권장한지 않는다.)
data.to_csv('자동차데이터.csv',index=False, encoding='cp949')

