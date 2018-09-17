#  # #  #   To get the sorted list
#
# # # ls -ltcr >> list
#
#
# import os
# videoNames=[]
# path = '/home/dan/Documents'
# listOfFiles = os.listdir(path)
# for videoName in listOfFiles:
#     videoNames.append(videoName)
# # print ("\n".join(videoNames))
#
# svideoNames = []
# jabber = open ("/home/dan/list","r")
# for v in jabber:
#     v = v[44::]
#     svideoNames.append(v.strip('\n'))
# jabber.close
#
# del svideoNames[0]
#
#
# videorename =""
# for videoName in videoNames:
#     i =1
#     for svideoName in svideoNames:
#         if (videoName==svideoName):
#             if i<10:
#                 videorename = "0"+str(i)+"_"+svideoName
#             else:
#                 videorename = str(i)+"_"+svideoName
#             videorename = videorename.replace(" ","")
#             os.rename(path +"/"+videoName,path +"/"+videorename )
#             # print (videorename+ "||" + videoName)
#         i=i+1
#
#
#
#
#
#
# #
# #
# #
# #
# #
# #
# # # cities = []
# # #
# # # with open("cities.txt", 'r') as city_file:
# # #     for city in city_file:
# # #         cities.append(city.strip('\n'))
# #
# #
# #
# #
# #
# # # jabber = open("/home/dan/Downloads/list.txt","r")
# # # for line in jabber:
# # #     print(line[44::],end="")			# here end='' has no use '.' line as \n
# # #
# # # jabber.close()		# Here file should be colsed after use or else it will be corrupted
# #
# #
# #  # for city in city_file:
# # #         slist.append(v)
