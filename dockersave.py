import re
import os
import subprocess

if __name__ == "__main__":
    os.system('rm -rf /tmp/saved-docker-images')
    os.system('mkdir -p /tmp/saved-docker-images')
    p = subprocess.Popen('docker images', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.readline())
    for line in p.stdout.readlines():
        print(line)
        m = re.split(r'\s+', line)
        print(m)
        if len(m) < 2:
            continue

        # image name
        iname = m[0]
        # tag name
        itag = m[1]

        # tar package name
        tarname = iname.split('/')[-1]
        print(tarname)
        tarball = tarname + '.tar'
        ifull = iname + ':' + itag
        #save
        cmd = 'docker save -o ' + tarball + ' ' + ifull
        print(cmd)
        os.system(cmd)
        #compress
        cmd = 'tar czvf ' + tarball + '.gz ' + tarball + '; rm ' + tarball
        print(cmd)
        os.system(cmd)

        os.system('mv %s.gz /tmp/saved-docker-images/'%tarball)


    retval = p.wait()
