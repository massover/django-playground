# Django Playground

<p>Django Playground runs your python code client side directly in your browser using <a href="https://pyscript.net/">pyscript</a>. There is no server.</p>

<p>When this website is launched in your browser, it runs some initialization code in your browser to:</p>

<ul>
    <li>Create a model
        <pre>
        class Dog(models.Model):
            name = models.TextField()
        </pre>
    </li>
    <li>Configure django to work with an in memory sqlite database in your browser</li>
    <li>
        <a href="https://docs.djangoproject.com/en/4.1/ref/django-admin/#cmdoption-migrate-run-syncdb">
            Migrate with syncdb
        </a>
        to create the table in the sqlite database
    </li>
</ul>

## Local development

```bash
    open index.html
```