# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：search.py
@Author  ：Yunzhong Luo 
@Date    ：2020/12/16 8:04 下午 
'''

from django.db import connection
class Search:
    def __init__(self):
        self.cursor = connection.cursor()

    def loginSearch(self, account):
        sql = """
              SELECT user_pswd, type_id, user_id FROM USER WHERE user_name = '{}'     
        """
        sql = sql.format(account)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def _dicAll(self, data):
        dic = [
            # Baisc Info
            'basic_name',
            'basic_neighbourhood',
            'basic_web',
            'basic_img',
            'basic_summary',
            'basic_price',
            'basic_space',
            # Host Info
            'host_name',
            'host_since',
            'host_local',
            'host_img',
            'host_about',
            # Room Detail
            'room_property',
            'room_room',
            'room_accommodates',
            'room_bathrooms',
            'room_bedrooms',
            'room_beds',
            # Location 
            'loc_lat',
            'loc_lon',
            # Review
            'review_rating',
            'review_accuracy',
            'review_clean',
            'review_checkin',
            'review_communication',
            'review_locations',
            'review_value'
        ]
        res = [dict(zip(dic, row)) for row in data]
        return res

    def allInfo(self):
        sql = """
               SELECT g.name, g.neighbourhood_id, g.listing_url, g.picture_url, g.summary, g.price, g.space,
               h.host_name, h.host_since, h.host_location, h.host_picture_url, h.host_about,
               r.property_type_id, r.room_type_id, r.accommodates, r.bathrooms, r.bedrooms, r.beds,
               l.latitude, l.longitude,
               re.rating, re.accuracy, re.cleanliness, re.checkin, re.communication, re.location, re.value
               FROM ROOM_GENERAL as g
               LEFT JOIN HOST as h ON g.host_id = h.host_id
               LEFT JOIN ROOM_DETAIL as r ON g.id = r.id
               LEFT JOIN SPECIFIC_LOCATION as l ON g.id = l.id 
               LEFT JOIN REVIEW_SUMMARY as re ON g.id = re.id
               """
        self.cursor.execute(sql)
        return self._dicAll(self.cursor.fetchall())

    def _userConditon(self, data, emptyDic):
        conditionList = []
        # Set Where Clause
        for k, v in emptyDic.items():
            if v:
                if k == 'price':
                    clause = '(g.price > ' + str(data[k][0]) + ' AND g.price < ' + str(data[k][1]) + ')'
                elif k == 'mark':
                    clause = '(re.rating > ' + str(data[k][0]) + ' AND re.rating < ' + str(data[k][1]) + ')'
                elif k == 'accom':
                    clause = 'r.accommodates = ' + str(data[k])
                elif k == 'bathroom':
                    clause = 'r.bathrooms = ' + str(data[k])
                elif k == 'bedroom':
                    clause = 'r.bedrooms = ' + str(data[k])
                elif k == 'roomType':
                    clause = 'r.room_type_id = ' + str(data[k])
                elif k == 'propType':
                    clause = 'r.property_type_id = ' + str(data[k])
                conditionList.append(clause)
        # Gather
        return ' AND '.join(conditionList)

    def userSearch(self, data, emptyDic):
        basicSQL = """ 
               SELECT g.name, g.neighbourhood_id, g.listing_url, g.picture_url, g.summary, g.price, g.space,
               h.host_name, h.host_since, h.host_location, h.host_picture_url, h.host_about,
               r.property_type_id, r.room_type_id, r.accommodates, r.bathrooms, r.bedrooms, r.beds,
               l.latitude, l.longitude,
               re.rating, re.accuracy, re.cleanliness, re.checkin, re.communication, re.location, re.value
               FROM ROOM_GENERAL as g
               LEFT JOIN HOST as h ON g.host_id = h.host_id
               LEFT JOIN ROOM_DETAIL as r ON g.id = r.id
               LEFT JOIN SPECIFIC_LOCATION as l ON g.id = l.id 
               LEFT JOIN REVIEW_SUMMARY as re ON g.id = re.id
               """
        condition = self._userConditon(data, emptyDic)
        finalSQL = basicSQL + ' WHERE ' + condition
        self.cursor.execute(finalSQL)
        return self._dicAll(self.cursor.fetchall())

    def _dicHost(self, data):
        dic = [
            # Host Info
            'img',
            'name',
            'since',
            'location',
            'about',
            'repTime',
            'repRate',
            'acprate',
            'superhost',
            'id'
        ]
        res = [dict(zip(dic, row)) for row in data]
        return res

    def hostSearch(self, id):
        sql = '''
            SELECT host_picture_url, host_name, host_since, host_location, host_about, host_response_time, 
            host_response_rate, host_acceptance_rate, host_is_superhost, host_id
            FROM HOST 
            WHERE host_id = {} 
        '''
        sql = sql.format(id)
        self.cursor.execute(sql)
        return self._dicHost(self.cursor.fetchall())

    def hostUpdate(self, id, name, intro):
        sql = '''
            UPDATE HOST SET host_name = '{}', host_about = '{}' WHERE host_id = {}
        '''
        sql = sql.format(name, intro, id)
        self.cursor.execute(sql)
        try:
            self.cursor.execute("commit")
        except Exception as e:
            raise e
        return 1

    def test(self):
        print('test')




