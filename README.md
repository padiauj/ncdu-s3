# ncdu-s3
### Python 3 compatible
The original, https://github.com/EverythingMe/ncdu-s3, is no longer maintained, and lacks support for Python 3. This fork serves as a source for a Python 3 compatible version for ncdu-s3.

This tool generates [ncdu](http://dev.yorhel.nl/ncdu) formatted JSON data file for S3 buckets. 

![Screenshot](screenshots.gif)

# Usage
```bash
$ sudo pip3 install git+git://github.com/padiauj/ncdu-s3.git
$ ncdu-s3 s3://my-bucket my-bucket.json
$ ncdu -f my-bucket.json
```

Please note you need boto configured for your user before using this tool.  
See how to configure boto [here](http://boto3.readthedocs.org/en/latest/guide/configuration.html)
