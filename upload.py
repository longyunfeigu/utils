import paramiko
import datetime
import os

hostname = '127.0.0.1'

username = 'admin'

password = '123456'

port = 22


def upload(local_dir, remote_dir):

    try:

        t = paramiko.Transport((hostname, port))

        t.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(t)

        print('upload file start %s ' % datetime.datetime.now())

        for root, dirs, files in os.walk(local_dir):

            for filespath in files:

                local_file = os.path.join(root, filespath)
                remote_file = local_file.replace(local_dir, remote_dir)

                try:
                    sftp.put(local_file, remote_file)
                except Exception:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                print("upload %s to remote %s" % (local_file, remote_file))

            for name in dirs:
                local_path = os.path.join(root, name)
                remote_path = local_path.replace(local_dir, remote_dir)
                try:
                    sftp.mkdir(remote_path)
                    print("mkdir path %s" % remote_path)
                except Exception as e:
                    print(e)

        print('upload file success %s ' % datetime.datetime.now())
        t.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':

    local_dir = '/home/xxx'

    remote_dir = '/home/yyy'

    upload(local_dir, remote_dir)
