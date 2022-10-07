import pandas as pd
import os
from num_alg_pre_block_function import *
from num_alg_mid_block_function import *
from num_alg_post_block_function import *

from mea_geo_pre_block_function import *
from mea_geo_mid_block_function import *
from mea_geo_post_block_function import *

from sta_pro_pre_block_function import *
from sta_pro_mid_block_function import *
from sta_pro_post_block_function import *

def listDir(dir):
    filenames = os.listdir(dir)
    return filenames

school_name = input("Please enter the name of the school you would like to format:")

general_num_alg_filenames = listDir("./general sweep raw files/"+str(school_name.title())+"/num-alg/")
general_mea_geo_filenames = listDir("./general sweep raw files/"+str(school_name.title())+"/mea-geo/")
general_sta_pro_filenames = listDir("./general sweep raw files/"+str(school_name.title())+"/sta-pro/")
achievement_filenames = listDir("./achievement raw files/"+str(school_name.title()))
classlist_filenames = listDir("./classlist/"+str(school_name.title()))

classlist_value = pd.read_excel("./classlist/"+str(school_name.title()+"/"+classlist_filenames[0]), header=0)
classlist_value = pd.DataFrame(classlist_value)
classlist_value = classlist_value.fillna("")
classlist_value = classlist_value.values.tolist()

general_file_num_alg_dict = {}
n=0
while n < len(general_num_alg_filenames):
    key = general_num_alg_filenames[n]
    general_files = pd.read_excel("./general sweep raw files/"+str(school_name.title())+"/num-alg/"+str(general_num_alg_filenames[n]), sheet_name="Data View", header=3) 
    general_files = pd.DataFrame(general_files)
    general_files = general_files.fillna("")
    value = general_files.values.tolist()
    general_file_num_alg_dict[key] = value
    n+=1

general_file_mea_geo_dict = {}
n=0
while n < len(general_mea_geo_filenames):
    key = general_mea_geo_filenames[n]
    general_files = pd.read_excel("./general sweep raw files/"+str(school_name.title())+"/mea-geo/"+str(general_mea_geo_filenames[n]), sheet_name="Data View", header=3) 
    general_files = pd.DataFrame(general_files)
    general_files = general_files.fillna("")
    value = general_files.values.tolist()
    general_file_mea_geo_dict[key] = value
    n+=1

general_file_sta_pro_dict = {}
n=0
while n < len(general_sta_pro_filenames):
    key = general_sta_pro_filenames[n]
    general_files = pd.read_excel("./general sweep raw files/"+str(school_name.title())+"/sta-pro/"+str(general_sta_pro_filenames[n]), sheet_name="Data View", header=3) 
    general_files = pd.DataFrame(general_files)
    general_files = general_files.fillna("")
    value = general_files.values.tolist()
    general_file_sta_pro_dict[key] = value
    n+=1

achievement_file_dict = {}
n=0
while n < len(achievement_filenames):
    key = achievement_filenames[n]
    achievement_files = pd.read_excel("./achievement raw files/"+str(school_name.title())+"/"+str(achievement_filenames[n]), header=0)
    achievement_files = pd.DataFrame(achievement_files)
    achievement_files = achievement_files.fillna("")
    value = achievement_files.values.tolist()
    achievement_file_dict[key] = value
    n+=1

reference_num_alg_vccodes_dict = {}
n=0
while n < len(general_num_alg_filenames):
    key = general_num_alg_filenames[n]
    reference_num_alg_vccodes_list = []
    for i in range(4,len(general_file_num_alg_dict[general_num_alg_filenames[n]][0])):
        reference_num_alg_vccodes_list.append(general_file_num_alg_dict[general_num_alg_filenames[n]][0][i].split(" -")[0])
    value = reference_num_alg_vccodes_list
    reference_num_alg_vccodes_dict[key] = value
    n+=1

reference_mea_geo_vccodes_dict = {}
n=0
while n < len(general_mea_geo_filenames):
    key = general_mea_geo_filenames[n]
    reference_mea_geo_vccodes_list = []
    for i in range(4,len(general_file_mea_geo_dict[general_mea_geo_filenames[n]][0])):
        reference_mea_geo_vccodes_list.append(general_file_mea_geo_dict[general_mea_geo_filenames[n]][0][i].split(" -")[0])
    value = reference_mea_geo_vccodes_list
    reference_mea_geo_vccodes_dict[key] = value
    n+=1

reference_sta_pro_vccodes_dict = {}
n=0
while n < len(general_sta_pro_filenames):
    key = general_sta_pro_filenames[n]
    reference_sta_pro_vccodes_list = []
    for i in range(4,len(general_file_sta_pro_dict[general_sta_pro_filenames[n]][0])):
        reference_sta_pro_vccodes_list.append(general_file_sta_pro_dict[general_sta_pro_filenames[n]][0][i].split(" -")[0])
    value = reference_sta_pro_vccodes_list
    reference_sta_pro_vccodes_dict[key] = value
    n+=1

num_alg_pre_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Number and Algebra" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "PRE":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"num-alg"
                num_alg_pre_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass


num_alg_mid_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Number and Algebra" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "MID":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"num-alg"
                num_alg_mid_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass


num_alg_post_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Number and Algebra" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "POST":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"num-alg"
                num_alg_post_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass

mea_geo_pre_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Measurement and Geometry" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "PRE":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"mea-geo"
                mea_geo_pre_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass


mea_geo_mid_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Measurement and Geometry" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "MID":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"mea-geo"
                mea_geo_mid_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass


mea_geo_post_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Measurement and Geometry" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "POST":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"mea-geo"
                mea_geo_post_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass

sta_pro_pre_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Statistics and Probability" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "PRE":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"sta-pro"
                sta_pro_pre_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass

sta_pro_mid_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Statistics and Probability" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "MID":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"sta-pro"
                sta_pro_mid_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass

sta_pro_post_raw_student_results_dict = {}
n=0
try:
    while n < len(achievement_filenames):
        for i in range(len(achievement_file_dict[achievement_filenames[n]])):
            if str(achievement_file_dict[achievement_filenames[n]][i][7]) == "General All" and str(achievement_file_dict[achievement_filenames[n]][i][6]) == "Statistics and Probability" and str(achievement_file_dict[achievement_filenames[n]][i][4]) == "POST":
                key = str(achievement_file_dict[achievement_filenames[n]][i][0]).title()+"-"+str(achievement_file_dict[achievement_filenames[n]][i][4])+"-"+"sta-pro"
                sta_pro_post_raw_student_results_dict[key] = [[achievement_file_dict[achievement_filenames[n]][i][0].title(),achievement_file_dict[achievement_filenames[n]][i][5],achievement_file_dict[achievement_filenames[n]][i][9],achievement_file_dict[achievement_filenames[n]][i][10]]]
            else:
                pass
        n+=1
except Exception as e:
    print(e)
    pass

codes_extract = pd.read_excel("./upload template.xlsx", sheet_name="Codes", header=None)
codes_extract = pd.DataFrame(codes_extract)
codes_extract_list = codes_extract.values.tolist()

student_results_extract = pd.read_excel("./upload template.xlsx", sheet_name="Student Results", header=None)
student_results_extract = pd.DataFrame(student_results_extract)
student_results_extract_list = student_results_extract.values.tolist()

student_reports_extract = pd.read_excel("./upload template.xlsx", sheet_name="Student Reports", header=None)
student_reports_extract = pd.DataFrame(student_reports_extract)
student_reports_extract_list = student_reports_extract.values.tolist()

#-----------------------------------------------Number and Algebra Export---------------------------------------------------------------------#

codes_extract_df, num_alg_pre_student_results_extract_df, num_alg_pre_student_reports_extract_df = num_alg_pre_block_function(num_alg_pre_raw_student_results_dict,general_num_alg_filenames,general_file_num_alg_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_num_alg_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, num_alg_mid_student_results_extract_df, num_alg_mid_student_reports_extract_df = num_alg_mid_block_function(num_alg_mid_raw_student_results_dict,general_num_alg_filenames,general_file_num_alg_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_num_alg_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, num_alg_post_student_results_extract_df, num_alg_post_student_reports_extract_df = num_alg_post_block_function(num_alg_post_raw_student_results_dict,general_num_alg_filenames,general_file_num_alg_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_num_alg_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)

school_name_with_underscore = school_name.title().replace(" ","_")

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Number_and_Algebra_Pre_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    num_alg_pre_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    num_alg_pre_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Number_and_Algebra_Mid_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    num_alg_mid_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    num_alg_mid_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Number_and_Algebra_Post_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    num_alg_post_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    num_alg_post_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)


#-----------------------------------------------Measurement and Geometry Export---------------------------------------------------------------------#

codes_extract_df, mea_geo_pre_student_results_extract_df, mea_geo_pre_student_reports_extract_df = mea_geo_pre_block_function(mea_geo_pre_raw_student_results_dict,general_mea_geo_filenames,general_file_mea_geo_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_mea_geo_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, mea_geo_mid_student_results_extract_df, mea_geo_mid_student_reports_extract_df = mea_geo_mid_block_function(mea_geo_mid_raw_student_results_dict,general_mea_geo_filenames,general_file_mea_geo_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_mea_geo_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, mea_geo_post_student_results_extract_df, mea_geo_post_student_reports_extract_df = mea_geo_post_block_function(mea_geo_post_raw_student_results_dict,general_mea_geo_filenames,general_file_mea_geo_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_mea_geo_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)

#We need to drop all the blank rows - investigate this

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Measurement_and_Geometry_Pre_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    mea_geo_pre_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    mea_geo_pre_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Measurement_and_Geometry_Mid_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    mea_geo_mid_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    mea_geo_mid_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Measurement_and_Geometry_Post_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    mea_geo_post_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    mea_geo_post_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)


#-----------------------------------------------Statistics and Probability Export---------------------------------------------------------------------#

codes_extract_df, sta_pro_pre_student_results_extract_df, sta_pro_pre_student_reports_extract_df = sta_pro_pre_block_function(sta_pro_pre_raw_student_results_dict,general_sta_pro_filenames,general_file_sta_pro_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_sta_pro_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, sta_pro_mid_student_results_extract_df, sta_pro_mid_student_reports_extract_df = sta_pro_mid_block_function(sta_pro_mid_raw_student_results_dict,general_sta_pro_filenames,general_file_sta_pro_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_sta_pro_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)
codes_extract_df, sta_pro_post_student_results_extract_df, sta_pro_post_student_reports_extract_df = sta_pro_post_block_function(sta_pro_post_raw_student_results_dict,general_sta_pro_filenames,general_file_sta_pro_dict,classlist_value,achievement_filenames,achievement_file_dict,reference_sta_pro_vccodes_dict,codes_extract_list,student_results_extract_list,student_reports_extract_list)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Statistics_and_Probability_Pre_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    sta_pro_pre_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    sta_pro_pre_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Statistics_and_Probability_Mid_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    sta_pro_mid_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    sta_pro_mid_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

with pd.ExcelWriter("./formatted folder/"+ school_name_with_underscore +"_Essentials_Assessment_Statistics_and_Probability_Post_Test.xlsx") as writer:
    codes_extract_df.to_excel(writer, sheet_name="Codes", index=False, header=0)
    sta_pro_post_student_results_extract_df.to_excel(writer, sheet_name="Student Results", index=False, header=0)
    sta_pro_post_student_reports_extract_df.to_excel(writer, sheet_name="Student Reports", index=False, header=0)

print("All done, please check the formatted folder for your files :)")




