import os
def replace(folder_path, old, new):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if(old.lower() in name.lower()):
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,name.lower().replace(old,new))
                os.rename(file_path, new_name)
You can use this function as follows −

replace('my_folder', 'IMG', 'Image')

for root, subs, files in os.walk("."):
    for file in files:
    date = re.search("\w*.-\w*.-\w*.",file)
    date_clean = date.group(0).strip()
    hour = re.search("hr\d", file)
    hour_clean = hour.group(0).strip()
    new_name = "Podcast-" + date_clean + "-" + hour_clean +".mp3"
    print "Changing",file,"to",new_name+"."
    os.rename(os.path.join(root, file), os.path.join(root, new_name))
