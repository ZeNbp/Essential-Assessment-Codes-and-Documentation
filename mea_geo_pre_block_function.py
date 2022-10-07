import pandas as pd
import os

#--------------------------------------------------------PRE-mea-geo FORMATTING BLOCK Part (a)-----------------------------------------------------

def mea_geo_pre_block_function(mea_geo_pre_raw_student_results_dict,general_mea_geo_filenames,
general_file_mea_geo_dict,
classlist_value,
achievement_filenames,
achievement_file_dict,
reference_mea_geo_vccodes_dict,
codes_extract_list,
student_results_extract_list,
student_reports_extract_list):

    mea_geo_pre_raw_student_results_output_list = []
    mea_geo_pre_raw_student_reports_output_list = []
    student_not_found_blank_list = ["Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found"]

    if len(mea_geo_pre_raw_student_results_dict) != 0:

        #checks for PRE results
        
        for x in range(len(general_mea_geo_filenames)):
            for y in range(4,len(general_file_mea_geo_dict[general_mea_geo_filenames[x]])):
                for z in range(len(classlist_value)):
                    try:
                        if general_file_mea_geo_dict[general_mea_geo_filenames[x]][y][1].title() == str(classlist_value[z][0])+" "+str(classlist_value[z][2]):
                            if mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[x]][y][1].title()+"-PRE-mea-geo"][0] != classlist_value[z]:                         
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[x]][y][1].title()+"-PRE-mea-geo"].insert(0,classlist_value[z])
                            else:
                                pass
                        else:
                            pass
                    except Exception as e:
                        #print(e)
                        pass

        for x in range(len(general_mea_geo_filenames)):
            for y in range(4,len(general_file_mea_geo_dict[general_mea_geo_filenames[x]])):
                try:
                    if len(mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[x]][y][1].title()+"-PRE-mea-geo"]) != 2:
                        mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[x]][y][1].title()+"-PRE-mea-geo"].insert(0,student_not_found_blank_list)
                    else:
                        pass
                except Exception as e:
                    #print(e)
                    pass

        for i in range(len(general_mea_geo_filenames)): #parses through each of the number-and-algebra filenames
            for j in range(4,len(general_file_mea_geo_dict[general_mea_geo_filenames[i]])): #parses through each of the number-and-algebra files
                for k in range(len(achievement_file_dict[achievement_filenames[0]])): #parses through each of the achievement results lines of the achievement file
                    if general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][2] == "PRE": #checks if the file is a "PRE" test result file
                        if general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title() == achievement_file_dict[achievement_filenames[0]][k][0].title(): #checks if the name is equivalent (i.e. matching) for the raw results list and the achievement list
                            if general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][2] == achievement_file_dict[achievement_filenames[0]][k][4] and achievement_file_dict[achievement_filenames[0]][k][6] == "Measurement and Geometry": #checks if the test period and test type is the same (e.g. "PRE" and "Measurement and Geometry")
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"].append(general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][4:len(general_file_mea_geo_dict[general_mea_geo_filenames[i]][j])])
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"].append(reference_mea_geo_vccodes_dict[general_mea_geo_filenames[i]])

                                for n in range(len(mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2])):                               
                                    mea_geo_pre_raw_student_results_output_list.append([
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][7],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][1][0],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][2],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][0],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][5],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][3],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][3][n],
                                    mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2][n],
                                    "PRE"])

                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2] = list(map(lambda x:0 if x=="" else x, mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2]))

                                mea_geo_pre_raw_student_reports_output_list.append([
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][7],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][1][0],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][2],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][0],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][5],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][0][3],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][1][1],
                                sum(mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2]),
                                len(mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][2]),
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][1][2],
                                mea_geo_pre_raw_student_results_dict[general_file_mea_geo_dict[general_mea_geo_filenames[i]][j][1].title()+"-PRE-mea-geo"][1][3],
                                "PRE"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
    else:
        pass

    for i in range(len(mea_geo_pre_raw_student_results_output_list)):
        mea_geo_pre_raw_student_results_output_list[i].append("Measurement and Geometry")

    for i in range(len(mea_geo_pre_raw_student_results_output_list)):
        for j in range(len(codes_extract_list)):
            if mea_geo_pre_raw_student_results_output_list[i][-4] == codes_extract_list[j][1]:
                mea_geo_pre_raw_student_results_output_list[i].append(codes_extract_list[j][0])
            else:
                pass

    for i in range(len(mea_geo_pre_raw_student_results_output_list)):
        if mea_geo_pre_raw_student_results_output_list[i][-4] == 1:
            mea_geo_pre_raw_student_results_output_list[i].insert(-4, "Correct")
            mea_geo_pre_raw_student_results_output_list[i].pop(-4)
        elif mea_geo_pre_raw_student_results_output_list[i][-4] == 0:
            mea_geo_pre_raw_student_results_output_list[i].insert(-4, "Incorrect")
            mea_geo_pre_raw_student_results_output_list[i].pop(-4)
        else:
            pass

    for i in range(len(mea_geo_pre_raw_student_reports_output_list)):
        mea_geo_pre_raw_student_reports_output_list[i].append("Measurement and Geometry")

    #--------------------------------------------------------PRE-mea-geo FORMATTING BLOCK Part (b)-----------------------------------------------------

    mea_geo_pre_student_results_extract_list = []
    mea_geo_pre_student_reports_extract_list = []

    for n in range(len(student_results_extract_list)):
        mea_geo_pre_student_results_extract_list.append(student_results_extract_list[n])

    for m in range(len(student_reports_extract_list)):
        mea_geo_pre_student_reports_extract_list.append(student_reports_extract_list[m])

    for i in range(len(mea_geo_pre_raw_student_results_output_list)):
        mea_geo_pre_student_results_extract_list.append(mea_geo_pre_raw_student_results_output_list[i])

    for j in range(len(mea_geo_pre_raw_student_reports_output_list)):
        mea_geo_pre_student_reports_extract_list.append(mea_geo_pre_raw_student_reports_output_list[j])


    mea_geo_pre_student_results_extract_df = pd.DataFrame(mea_geo_pre_student_results_extract_list)
    mea_geo_pre_student_reports_extract_df = pd.DataFrame(mea_geo_pre_student_reports_extract_list)
    mea_geo_pre_student_results_extract_df = mea_geo_pre_student_results_extract_df.drop_duplicates()
    mea_geo_pre_student_reports_extract_df = mea_geo_pre_student_reports_extract_df.drop_duplicates()

    codes_extract_df = pd.DataFrame(codes_extract_list)

    return codes_extract_df, mea_geo_pre_student_results_extract_df, mea_geo_pre_student_reports_extract_df

