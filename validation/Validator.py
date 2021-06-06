import re


def input_validation(form):
    email = True if 'email' in form else False
    url = True if 'url' in form else False
    atc = True if 'atc' in form else False

    if email:
        if email_validator(form['email']) != 'email':
            if url:
                if url_validator(form['url']) != 'url':
                    if atc:
                        if form['atc'] == 'on':
                            return True
                        else:
                            return 'atc'
                    else:
                        return 'atc'
                else:
                    return 'url'
            else:
                return 'url'
        else:
            return 'email'
    else:
        return 'email'


def email_validator(email):
    email_test = re.match(r'^([a-z0-9])([a-z0-9.]{2,50})(@)([a-z0-9-]{0,20})(\.)([a-z0-9]{1,20})$', email, re.I)
    if email_test:
        return True
    else:
        return 'email'


def url_validator(url):
    url_test = re.match(r'^(https://|http://)(www\.)?([a-z0-9:]{1,100})([.])([a-z0-9]{1,20})([:a-z0-9/._\-?&=+%#()]'
                        r'{0,1000})$', url, re.I)
    if url_test:
        return True
    else:
        return 'url'
