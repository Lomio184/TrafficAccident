import xml.etree.ElementTree as ET
import pickle

from common.common import *

class AccidentItem:
    def __init__(self, acc_year, occrrnc_dt, dght_cd, occrrnc_day_cd, dth_dnv_cnt, injpsn_cnt,
                 se_dnv_cnt, sl_dnv_cnt, wnd_dnv_cnt, occrrnc_lc_sido_cd, occrrnc_lc_sgg_cd,
                 acc_ty_lclas_cd, acc_ty_mlsfc_cd, acc_ty_cd, aslt_vtr_cd, road_frm_lclas_cd,
                 road_frm_cd, wrngdo_isrty_vhcty_lclas_cd, dmge_isrty_vhcty_lclas_cd,
                 occrrnc_lc_x_crd, occrrnc_lc_y_crd, lo_crd, la_crd):
        self.acc_year = acc_year
        self.occrrnc_dt = occrrnc_dt
        self.dght_cd = dght_cd
        self.occrrnc_day_cd = occrrnc_day_cd
        self.dth_dnv_cnt = dth_dnv_cnt
        self.injpsn_cnt = injpsn_cnt
        self.se_dnv_cnt = se_dnv_cnt
        self.sl_dnv_cnt = sl_dnv_cnt
        self.wnd_dnv_cnt = wnd_dnv_cnt
        self.occrrnc_lc_sido_cd = occrrnc_lc_sido_cd
        self.occrrnc_lc_sgg_cd = occrrnc_lc_sgg_cd
        self.acc_ty_lclas_cd = acc_ty_lclas_cd
        self.acc_ty_mlsfc_cd = acc_ty_mlsfc_cd
        self.acc_ty_cd = acc_ty_cd
        self.aslt_vtr_cd = aslt_vtr_cd
        self.road_frm_lclas_cd = road_frm_lclas_cd
        self.road_frm_cd = road_frm_cd
        self.wrngdo_isrty_vhcty_lclas_cd = wrngdo_isrty_vhcty_lclas_cd
        self.dmge_isrty_vhcty_lclas_cd = dmge_isrty_vhcty_lclas_cd
        self.occrrnc_lc_x_crd = occrrnc_lc_x_crd
        self.occrrnc_lc_y_crd = occrrnc_lc_y_crd
        self.lo_crd = lo_crd
        self.la_crd = la_crd
        self.uuid   = None

    def __repr__(self):
        return f"<AccidentItem acc_year={self.acc_year}, occrrnc_dt={self.occrrnc_dt}, dth_dnv_cnt={self.dth_dnv_cnt}>, lo_crd : {self.lo_crd}, la_crd : {self.la_crd}"
    



# XML 데이터 파싱 함수
def parse_accident_data(items, xml_data):
    root = ET.fromstring(xml_data)
    
    for item in root.findall(".//item"):
        accident_item = AccidentItem(
            acc_year=item.find("acc_year").text,
            occrrnc_dt=item.find("occrrnc_dt").text,
            dght_cd=item.find("dght_cd").text,
            occrrnc_day_cd=item.find("occrrnc_day_cd").text,
            dth_dnv_cnt=int(item.find("dth_dnv_cnt").text),
            injpsn_cnt=int(item.find("injpsn_cnt").text),
            se_dnv_cnt=int(item.find("se_dnv_cnt").text),
            sl_dnv_cnt=int(item.find("sl_dnv_cnt").text),
            wnd_dnv_cnt=int(item.find("wnd_dnv_cnt").text),
            occrrnc_lc_sido_cd=item.find("occrrnc_lc_sido_cd").text,
            occrrnc_lc_sgg_cd=item.find("occrrnc_lc_sgg_cd").text,
            acc_ty_lclas_cd=item.find("acc_ty_lclas_cd").text,
            acc_ty_mlsfc_cd=item.find("acc_ty_mlsfc_cd").text,
            acc_ty_cd=item.find("acc_ty_cd").text,
            aslt_vtr_cd=item.find("aslt_vtr_cd").text,
            road_frm_lclas_cd=item.find("road_frm_lclas_cd").text,
            road_frm_cd=item.find("road_frm_cd").text,
            wrngdo_isrty_vhcty_lclas_cd=item.find("wrngdo_isrty_vhcty_lclas_cd").text,
            dmge_isrty_vhcty_lclas_cd=item.find("dmge_isrty_vhcty_lclas_cd").text,
            occrrnc_lc_x_crd=item.find("occrrnc_lc_x_crd").text.strip(),
            occrrnc_lc_y_crd=item.find("occrrnc_lc_y_crd").text.strip(),
            lo_crd=float(item.find("lo_crd").text),
            la_crd=float(item.find("la_crd").text)
        )
        items.append(accident_item)
    
    return items

def parsing_xml_query_data():
    data_arr = []
    print("Parsing XML Traffic Accident Data")
    
    try:
        # 2021~2023 년 사이의 교통사고 데이터 조회
        for yearVal in year:
            params['searchYear'] = yearVal
            
            for guGunVal in seoul_guGun_request_val_list:
                # 매 파라미터마다 구군 값 변경 
                params['guGun'] = guGunVal
                
                # GET 요청 보내기
                response = requests.get(url, params=params)
                
                # 응답 상태 코드 확인
                response.raise_for_status()  # 200 OK가 아닌 경우 예외 발생
                
                # XML 데이터 파싱
                parse_accident_data(data_arr, response.text)

        # 파싱된 객체 출력
        with open("traffic_accident.pkl", "wb") as file:
            pickle.dump( data_arr, file )
        file.close()
        
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
        
# 덤핑시킨 교통 사고 데이터 로딩.        
def load_parsing_data():
    with open("traffic_accident.pkl", "rb") as file:
        dump_data = pickle.load( file )
        
    file.close()
    
    return dump_data