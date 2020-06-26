# zollege-lti-processors
Repo containing custom processors for Zollege LTI

This package uses the LTI Consumer XBlock interface to add extra parameters
in addition to the default LTI parameters.

## Usage
Install the pip package:

```
$ pip install git+https://github.com/eduNEXT/zollege-lti-processors.git
```

or in Open edX DevStack, clone this repo in the src folder and install it from there:

```
$ pip install -e /edx/src/zollege-lti-processors
```

Add the following settings to your `server-vars.yml` (or whatever method you configure your Open edX installation):

```yaml
EDXAPP_XBLOCK_SETTINGS:
  lti_consumer:
    parameter_processors:
      - 'zollege_lti.processors:personal_user_info'
      - 'zollege_lti.processors:course_info'
```

Restart the Open edX instance and it should be working.

### How to Test?
 - Set the LTI Passports to `test:test:secret` in the course advanced settings.
 - Add the `lti_consumer` to the advanced modules.
 - From the advanced modules create a new LTI module
 - Configure the module like the following:
   * URL: `https://lti.tools/saltire/tp`
   * LTI ID: `test`
   * Set **Send extra parameters** to `true`
