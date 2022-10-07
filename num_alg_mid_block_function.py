import pandas as pd
import os

#--------------------------------------------------------mid-Num-Alg FORMATTING BLOCK Part (a)-----------------------------------------------------

def num_alg_mid_block_function(num_alg_mid_raw_student_results_dict,general_num_alg_filenames,
general_file_num_alg_dict,
classlist_value,
achievement_filenames,
achievement_file_dict,
reference_num_alg_vccodes_dict,
codes_extract_list,
student_results_extract_list,
student_reports_extract_list):

    num_alg_mid_raw_student_results_output_list = []
    num_alg_mid_raw_student_reports_output_list = []
    student_not_found_blank_list = ["Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found"]

    if len(num_alg_mid_raw_student_results_dict) != 0:

        #checks for mid results
        
        for x in range(len(general_num_alg_filenames)):
            for y in range(4,len(general_file_num_alg_dict[general_num_alg_filenames[x]])):
                for z in range(len(classlist_value)):
                    try:
                        if general_file_num_alg_dict[general_num_alg_filenames[x]][y][1].title() == str(classlist_value[z][0])+" "+str(classlist_value[z][2]):
                            if num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[x]][y][1].title()+"-MID-num-alg"][0] != classlist_value[z]:
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[x]][y][1].title()+"-MID-num-alg"].insert(0,classlist_value[z])
                            else:
                                pass
                        else:
                            pass
                    except Exception as e:
                        #print(e)
                        #print("Error on top")
                        pass

        for x in range(len(general_num_alg_filenames)):
            for y in range(4,len(general_file_num_alg_dict[general_num_alg_filenames[x]])):
                try:
                    if len(num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[x]][y][1].title()+"-MID-num-alg"]) != 2:
                        num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[x]][y][1].title()+"-MID-num-alg"].insert(0,student_not_found_blank_list)
                    else:
                        pass
                except Exception as e:
                    #print(e)
                    pass
                    
        for i in range(len(general_num_alg_filenames)): #parses through each of the number-and-algebra filenames
            for j in range(4,len(general_file_num_alg_dict[general_num_alg_filenames[i]])): #parses through each of the number-and-algebra files
                for k in range(len(achievement_file_dict[achievement_filenames[0]])): #parses through each of the achievement results lines of the achievement file
                    if general_file_num_alg_dict[general_num_alg_filenames[i]][j][2] == "MID": #checks if the file is a "mid" test result file
                        if general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title() == achievement_file_dict[achievement_filenames[0]][k][0].title(): #checks if the name is equivalent (i.e. matching) for the raw results list and the achievement list
                            if general_file_num_alg_dict[general_num_alg_filenames[i]][j][2] == achievement_file_dict[achievement_filenames[0]][k][4] and achievement_file_dict[achievement_filenames[0]][k][6] == "Number and Algebra": #checks if the test period and test type is the same (e.g. "mid" and "Number and Algebra")
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"].append(general_file_num_alg_dict[general_num_alg_filenames[i]][j][4:len(general_file_num_alg_dict[general_num_alg_filenames[i]][j])])
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"].append(reference_num_alg_vccodes_dict[general_num_alg_filenames[i]])

                                for n in range(len(num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2])):                               
                                    num_alg_mid_raw_student_results_output_list.append([
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][7],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][1][0],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][2],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][0],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][5],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][3],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][3][n],
                                    num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2][n],
                                    "MID"])

                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2] = list(map(lambda x:0 if x=="" else x, num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2]))

                                num_alg_mid_raw_student_reports_output_list.append([
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][7],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][1][0],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][2],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][0],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][5],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][0][3],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][1][1],
                                sum(num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2]),
                                len(num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][2]),
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][1][2],
                                num_alg_mid_raw_student_results_dict[general_file_num_alg_dict[general_num_alg_filenames[i]][j][1].title()+"-MID-num-alg"][1][3],
                                "MID"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
    else:
        pass

    for i in range(len(num_alg_mid_raw_student_results_output_list)):
        num_alg_mid_raw_student_results_output_list[i].append("Number and Algebra")

    for i in range(len(num_alg_mid_raw_student_results_output_list)):
        for j in range(len(codes_extract_list)):
            if num_alg_mid_raw_student_results_output_list[i][-4] == codes_extract_list[j][1]:
                num_alg_mid_raw_student_results_output_list[i].append(codes_extract_list[j][0])
            else:
                pass

    for i in range(len(num_alg_mid_raw_student_results_output_list)):
        if num_alg_mid_raw_student_results_output_list[i][-4] == 1:
            num_alg_mid_raw_student_results_output_list[i].insert(-4, "Correct")
            num_alg_mid_raw_student_results_output_list[i].pop(-4)
        elif num_alg_mid_raw_student_results_output_list[i][-4] == 0:
            num_alg_mid_raw_student_results_output_list[i].insert(-4, "Incorrect")
            num_alg_mid_raw_student_results_output_list[i].pop(-4)
        else:
            pass

    for i in range(len(num_alg_mid_raw_student_reports_output_list)):
        num_alg_mid_raw_student_reports_output_list[i].append("Number and Algebra")

    #--------------------------------------------------------mid-Num-Alg FORMATTING BLOCK Part (b)-----------------------------------------------------

    num_alg_mid_student_results_extract_list = []
    num_alg_mid_student_reports_extract_list = []

    for n in range(len(student_results_extract_list)):
        num_alg_mid_student_results_extract_list.append(student_results_extract_list[n])

    for m in range(len(student_reports_extract_list)):
        num_alg_mid_student_reports_extract_list.append(student_reports_extract_list[m])

    for i in range(len(num_alg_mid_raw_student_results_output_list)):
        num_alg_mid_student_results_extract_list.append(num_alg_mid_raw_student_results_output_list[i])

    for j in range(len(num_alg_mid_raw_student_reports_output_list)):
        num_alg_mid_student_reports_extract_list.append(num_alg_mid_raw_student_reports_output_list[j])


    num_alg_mid_student_results_extract_df = pd.DataFrame(num_alg_mid_student_results_extract_list)
    num_alg_mid_student_reports_extract_df = pd.DataFrame(num_alg_mid_student_reports_extract_list)
    num_alg_mid_student_results_extract_df = num_alg_mid_student_results_extract_df.drop_duplicates()
    num_alg_mid_student_reports_extract_df = num_alg_mid_student_reports_extract_df.drop_duplicates()

    codes_extract_df = pd.DataFrame(codes_extract_list)

    return codes_extract_df, num_alg_mid_student_results_extract_df, num_alg_mid_student_reports_extract_df

