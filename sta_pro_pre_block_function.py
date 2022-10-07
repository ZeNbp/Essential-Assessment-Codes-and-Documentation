import pandas as pd
import os

#--------------------------------------------------------PRE-sta-pro FORMATTING BLOCK Part (a)-----------------------------------------------------

def sta_pro_pre_block_function(sta_pro_pre_raw_student_results_dict,general_sta_pro_filenames,
general_file_sta_pro_dict,
classlist_value,
achievement_filenames,
achievement_file_dict,
reference_sta_pro_vccodes_dict,
codes_extract_list,
student_results_extract_list,
student_reports_extract_list):

    sta_pro_pre_raw_student_results_output_list = []
    sta_pro_pre_raw_student_reports_output_list = []
    student_not_found_blank_list = ["Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found"]

    if len(sta_pro_pre_raw_student_results_dict) != 0:

        #checks for PRE results
        
        for x in range(len(general_sta_pro_filenames)):
            for y in range(4,len(general_file_sta_pro_dict[general_sta_pro_filenames[x]])):
                for z in range(len(classlist_value)):
                    try:
                        if general_file_sta_pro_dict[general_sta_pro_filenames[x]][y][1].title() == str(classlist_value[z][0])+" "+str(classlist_value[z][2]):
                            if sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[x]][y][1].title()+"-PRE-sta-pro"][0] != classlist_value[z]:                       
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[x]][y][1].title()+"-PRE-sta-pro"].insert(0,classlist_value[z])
                            else:
                                pass
                        else:
                            pass
                    except Exception as e:
                        #print(e)
                        pass

        for x in range(len(general_sta_pro_filenames)):
            for y in range(4,len(general_file_sta_pro_dict[general_sta_pro_filenames[x]])):
                try:
                    if len(sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[x]][y][1].title()+"-PRE-sta-pro"]) != 2:
                        sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[x]][y][1].title()+"-PRE-sta-pro"].insert(0,student_not_found_blank_list)
                    else:
                        pass
                except Exception as e:
                    #print(e)
                    pass

        for i in range(len(general_sta_pro_filenames)): #parses through each of the number-and-algebra filenames
            for j in range(4,len(general_file_sta_pro_dict[general_sta_pro_filenames[i]])): #parses through each of the number-and-algebra files
                for k in range(len(achievement_file_dict[achievement_filenames[0]])): #parses through each of the achievement results lines of the achievement file
                    if general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][2] == "PRE": #checks if the file is a "PRE" test result file
                        if general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title() == achievement_file_dict[achievement_filenames[0]][k][0].title(): #checks if the name is equivalent (i.e. matching) for the raw results list and the achievement list
                            if general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][2] == achievement_file_dict[achievement_filenames[0]][k][4] and achievement_file_dict[achievement_filenames[0]][k][6] == "Statistics and Probability": #checks if the test period and test type is the same (e.g. "PRE" and "Statistics and Probability")
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"].append(general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][4:len(general_file_sta_pro_dict[general_sta_pro_filenames[i]][j])])
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"].append(reference_sta_pro_vccodes_dict[general_sta_pro_filenames[i]])

                                for n in range(len(sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2])):                               
                                    sta_pro_pre_raw_student_results_output_list.append([
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][7],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][1][0],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][2],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][0],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][5],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][3],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][3][n],
                                    sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2][n],
                                    "PRE"])

                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2] = list(map(lambda x:0 if x=="" else x, sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2]))

                                sta_pro_pre_raw_student_reports_output_list.append([
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][7],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][1][0],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][2],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][0],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][5],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][0][3],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][1][1],
                                sum(sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2]),
                                len(sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][2]),
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][1][2],
                                sta_pro_pre_raw_student_results_dict[general_file_sta_pro_dict[general_sta_pro_filenames[i]][j][1].title()+"-PRE-sta-pro"][1][3],
                                "PRE"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
    else:
        pass

    for i in range(len(sta_pro_pre_raw_student_results_output_list)):
        sta_pro_pre_raw_student_results_output_list[i].append("Statistics and Probability")

    for i in range(len(sta_pro_pre_raw_student_results_output_list)):
        for j in range(len(codes_extract_list)):
            if sta_pro_pre_raw_student_results_output_list[i][-4] == codes_extract_list[j][1]:
                sta_pro_pre_raw_student_results_output_list[i].append(codes_extract_list[j][0])
            else:
                pass

    for i in range(len(sta_pro_pre_raw_student_results_output_list)):
        if sta_pro_pre_raw_student_results_output_list[i][-4] == 1:
            sta_pro_pre_raw_student_results_output_list[i].insert(-4, "Correct")
            sta_pro_pre_raw_student_results_output_list[i].pop(-4)
        elif sta_pro_pre_raw_student_results_output_list[i][-4] == 0:
            sta_pro_pre_raw_student_results_output_list[i].insert(-4, "Incorrect")
            sta_pro_pre_raw_student_results_output_list[i].pop(-4)
        else:
            pass

    for i in range(len(sta_pro_pre_raw_student_reports_output_list)):
        sta_pro_pre_raw_student_reports_output_list[i].append("Statistics and Probability")

    #--------------------------------------------------------PRE-sta-pro FORMATTING BLOCK Part (b)-----------------------------------------------------

    sta_pro_pre_student_results_extract_list = []
    sta_pro_pre_student_reports_extract_list = []

    for n in range(len(student_results_extract_list)):
        sta_pro_pre_student_results_extract_list.append(student_results_extract_list[n])

    for m in range(len(student_reports_extract_list)):
        sta_pro_pre_student_reports_extract_list.append(student_reports_extract_list[m])

    for i in range(len(sta_pro_pre_raw_student_results_output_list)):
        sta_pro_pre_student_results_extract_list.append(sta_pro_pre_raw_student_results_output_list[i])

    for j in range(len(sta_pro_pre_raw_student_reports_output_list)):
        sta_pro_pre_student_reports_extract_list.append(sta_pro_pre_raw_student_reports_output_list[j])


    sta_pro_pre_student_results_extract_df = pd.DataFrame(sta_pro_pre_student_results_extract_list)
    sta_pro_pre_student_reports_extract_df = pd.DataFrame(sta_pro_pre_student_reports_extract_list)
    sta_pro_pre_student_results_extract_df = sta_pro_pre_student_results_extract_df.drop_duplicates()
    sta_pro_pre_student_reports_extract_df = sta_pro_pre_student_reports_extract_df.drop_duplicates()

    codes_extract_df = pd.DataFrame(codes_extract_list)

    return codes_extract_df, sta_pro_pre_student_results_extract_df, sta_pro_pre_student_reports_extract_df

