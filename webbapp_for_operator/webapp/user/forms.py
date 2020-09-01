from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StartForm(FlaskForm):
    start_form = StringField('Start', render_kw={"class": "alert alert-secondary"})


class RequestsForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()], render_kw={"class": "form-control"})
    product = StringField('product', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_add = StringField('date add', validators=[DataRequired()], render_kw={"class": "form-control"})
    status_request = StringField('status_request', validators=[DataRequired()], render_kw={"class": "form-control"})
    first_name_client = StringField('first name', validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name_client = StringField('last name', validators=[DataRequired()], render_kw={"class": "form-control"})
    phone_client = StringField('phone', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_series = StringField('passport_series', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_number = StringField('passport_number', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Status', render_kw={"class": "btn btn-secondary dropdown-toggle"})
    submit_filter_all = SubmitField('Requests all', render_kw={"class": "btn btn-secondary dropdown-toggle"})
    submit_filter_done = SubmitField('Requests done', render_kw={"class": "btn btn-success dropdown-toggle"})
    submit_filter_considers = SubmitField('Requests considers', render_kw={"class": "btn btn-warning dropdown-toggle"})
    submit_filter_refused = SubmitField('Requests refused', render_kw={"class": "btn btn-danger dropdown-toggle"})


class Request_clientForm(FlaskForm):
    id = StringField('Номер заявки', validators=[DataRequired()], render_kw={"class": "form-control"})
    username = StringField('Никнейм в мессенджере', validators=[DataRequired()], render_kw={"class": "form-control"})
    service = StringField('Банковский продукт', validators=[DataRequired()], render_kw={"class": "form-control"})
    proposal = StringField('Тип банковского продукта', validators=[DataRequired()], render_kw={"class": "form-control"})
    status = StringField('Статус заявки', validators=[DataRequired()], render_kw={"class": "form-control"})
    chat_id = StringField('ID чата в телеграмм', validators=[DataRequired()], render_kw={"class": "form-control"})
    full_name = StringField('ФИО', validators=[DataRequired()], render_kw={"class": "form-control"})
    birthdate = StringField('Дата рождения', validators=[DataRequired()], render_kw={"class": "form-control"})
    birthplace = StringField('Место рождения', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_number = StringField('Серия номер паспорта', validators=[DataRequired()], render_kw={"class": "form-control"})
    department_code = StringField('Код подразделения', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_of_issue = StringField('Дата выдачи', validators=[DataRequired()], render_kw={"class": "form-control"})
    issued_by = StringField('Организация выдавшая документ', validators=[DataRequired()], render_kw={"class": "form-control"})
    address = StringField('Адрес регистрации', validators=[DataRequired()], render_kw={"class": "form-control"})
    actual_address = StringField('Адрес проживания', validators=[DataRequired()], render_kw={"class": "form-control"})
    i_c = StringField('СНИЛС', validators=[DataRequired()], render_kw={"class": "form-control"})
    phone_number = StringField('Номер телефона', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Адрес эл.почты', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit_update = SubmitField('Update', render_kw={"class": "btn btn-warning"})
    submit_accept = SubmitField('Accept', render_kw={"class": "btn btn-success"})
    submit_reject = SubmitField('Reject', render_kw={"class": "btn btn-danger"})
    submit_unchanged = SubmitField('Back', render_kw={"class": "btn btn-secondary"})


