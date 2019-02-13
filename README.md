cf-macro-hello
--------------

"Hello World" CloudFormation macro.

Usage:

1. create zip for lambda: `zip -9 src.zip index.py`
2. upload zip to S3: `aws s3 cp src.zip s3://some/where/src.zip`
3. edit deploy-macro.yml; change S3 permissions (optional, not used in this example) and CodeUri
4. create stack for deploy-macro.yml
5. the macro is now live; example template: hello.yml

This macro reads the original template and replaces an upper-level key Hello with a couple of instances.
