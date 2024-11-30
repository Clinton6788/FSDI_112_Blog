# Mini Challenge 2
## Overriding templates
### Acceptance Criteria
0. Add the following line to `config/settings.py`: `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`
1. Generate a template for your sign up view such that users can leverage it to create new accounts (and then login).
2. Test the password reset feature then:
2.1. Generate the following templates for the built-in password reset feature:
2.1.1. password_reset_form.html - this form allows us to submit an email address to receive password reset instructions
2.1.2. password_reset_done.html - this template simply confirms the successfull submittal of the previous form
2.1.3. password_reset_confirm.html - this *form* allows us to set a new password
2.1.4. password_reset_complete.html - this template simply confirms that we successfully set a new password
3. Add anchor tags on your base template (or wherever you see fit) to ensure users can access the new features you've added.
# Note
You do not have to override the email templates but if you want to:
the subject name is `registration/password_email_subject.txt`
and the email body is `registration/password_reset_email.html`

                <a class="nav-link" href="{% url 'list' %}">Posts</a>
                <a class="nav-link" href="{% url 'new' %}">New Post</a>
                <a class="nav-link" href="{% url 'about' %}">About</a>
                {% if user.is_authenticated %}
                <form method="POST" action="{% url 'logout' %}">
                    {% csrf_token %}
                    <input type="submit" value="Log Out" class="nav-link" id="">
                </form>
                {% else %}
                <a class="nav-link" href="{% url 'login' %}">Log In</a>
                {% endif %}
