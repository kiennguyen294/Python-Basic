import subprocess

cmd = ['ps', '-ef']
ps = subprocess.Popen(cmd, stdout=subprocess.PIPE)

cmd = ['grep', 'python']
grep = subprocess.Popen(cmd, stdin=ps.stdout, stdout=subprocess.PIPE, encoding='utf-8')
ps.stdout.close()
outpt, _ = grep.communicate()
python_processes = outpt.split('\n')
print(python_processes)
