import subprocess

# Save the bash script to a file, e.g., script.sh
# Make sure to give it execute permissions with `chmod +x script.sh`

# Run the bash script
process = subprocess.Popen(['./bestSoFar.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read the output and errors, if any
output, error = process.communicate()

# Print the output
print(output.decode())
