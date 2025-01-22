import os
import glob
import datetime

# Set the source and destination folders
source = os.path.join(os.environ["USERPROFILE"], "Desktop")
destination = os.path.join(os.environ["USERPROFILE"], "Documents", "MyJpgs")

# Move all files with a .png, .jpg, .jpeg, or .webp extension from the source to the destination folder
for file in glob.glob(os.path.join(source, "*.png")) + glob.glob(os.path.join(source, "*.jpg")) + glob.glob(os.path.join(source, "*.jpeg")) + glob.glob(os.path.join(source, "*.webp")):
    filename, ext = os.path.splitext(os.path.basename(file))

    # Get the modified time of the file
    mtime = os.stat(file).st_mtime

    # Extract the month and year from the modified time
    month = datetime.datetime.fromtimestamp(mtime).strftime("%B")
    year = datetime.datetime.fromtimestamp(mtime).strftime("%Y")

    # Create a subfolder for the month and year
    subfolder = os.path.join(destination, "{}-{}".format(month, year))
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    # Set the target file path
    target = os.path.join(subfolder, "{}{}".format(filename, ext))

    # Check if the file already exists in the destination folder
    # If it does, append a number to the end of the file name to avoid a conflict
    if os.path.exists(target):
        count = 1
        while True:
            newtarget = os.path.join(subfolder, "{} ({}){}".format(filename, count, ext))
            if not os.path.exists(newtarget):
                break
            count += 1

        # Move the file to the new target
        os.rename(file, newtarget)
    else:
        # Move the file to the destination
        os.rename(file, target)

print("Done!")
