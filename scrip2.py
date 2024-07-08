import subprocess

process = subprocess.Popen(['./bestSoFar.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    output, error = process.communicate(timeout=10)  # wait for 10 seconds
except subprocess.TimeoutExpired:
    process.kill()  # kill the bash script
    output, error = process.communicate()

print(output.decode())
