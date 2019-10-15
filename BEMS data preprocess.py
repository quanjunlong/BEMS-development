# -*- coding: utf-8 -*-
"""
EAN BEMS 데이터 전처리(핸들링)
작성일: 2019.10.08
작성자: 전준용
"""


"""
오라클 DB 접속 및 전력 데이터 추출
"""

# 모듈 가져오기
import cx_Oracle
import os
import pandas as pd
import datetime


#한글깨짐방지
os.environ["NLS_LANG"] = ".AL32UTF8"
START_VALUE = u"Unicode \u3042 3".encode('utf-8')
END_VALUE = u"Unicode \u3042 6".encode('utf-8')

#오라클DB 연결
con1 = cx_Oracle.connect("bemsdb/bemsdb@10.1.1.49:1521/eandb")
cursor = con1.cursor()

#데이터 추출
cursor.execute('select T_DATETIME, I_SUM, C_DESC from TB_RAWDATA order by T_DATETIME')
rawdata = pd.DataFrame(cursor.fetchall())
con1.close()
print(rawdata.loc[0:50])

"""
데이터 전처리
"""

#메인데이터 추출
rd_4 = rawdata.loc[rawdata[2].str.contains("4층 - 메인")]
rd_5 = rawdata.loc[rawdata[2].str.contains("5층 - 메인")]
rd_6 = rawdata.loc[rawdata[2].str.contains("6층 - 메인")]
rd_7 = rawdata.loc[rawdata[2].str.contains("7층 - 메인")]
rd_8 = rawdata.loc[rawdata[2].str.contains("8층 - 메인")]
rd_9 = rawdata.loc[rawdata[2].str.contains("9층 - 메인")]
rd_10 = rawdata.loc[rawdata[2].str.contains("10층 - 메인")]

#시간길이자르기
#rd_4[0] = rd_4[0].astype(str).str.slice(stop=16)
#time index 변환
rd_4[0] = pd.to_datetime(rd_4[0])
rd_4.index = rd_4[0]
#행제거
del rd_4[0], rd_4[2]
#시간단위에 따라 열 행 정렬
rd_count = rd_4.resample("H").first().diff()

print(rd_count)

"""
실내 온도, 습도 데이터 추출
"""

#데이터 추출
con1 = cx_Oracle.connect("bemsdb/bemsdb@10.1.1.49:1521/eandb")
cursor = con1.cursor()
cursor.execute('select T_DATETIME, C_SLAVE, I_TEMP, I_HUMI from TB_CO2 order by T_DATETIME')
rawdata_indoor = pd.DataFrame(cursor.fetchall())
con1.close()
print(rawdata_indoor.loc[0:50])

"""
실내 온도, 습도 데이터 전처리
"""

rwid_8 = rawdata_indoor.loc[rawdata_indoor[1].str.contains("8")]
rwid_8[0] = pd.to_datetime(rwid_8[0])
rwid_8.index = rwid_8[0]
del rwid_8[0], rwid_8[1]
rwid_8_count = rwid_8.resample("H").first()
rwid_8_count_rw = rwid_8_count["2018-09-11":]
