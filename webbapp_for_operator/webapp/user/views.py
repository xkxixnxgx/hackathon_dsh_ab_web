from flask import Blueprint, render_template, flash, redirect, url_for, request
from webapp.user.forms import RequestsForm, Request_clientForm

from webapp.db import posts
from bson.objectid import ObjectId
import crypto
from datetime import datetime

blueprint = Blueprint('user', __name__)


@blueprint.route('/requests', methods=['GET'])
def requests():
    title = 'Requests'
    form = RequestsForm()
    request_list = crypto.decrypt_all(list(posts.find()))
    return render_template('requests.html',
                           page_title=title,
                           request_list=request_list,
                           form=form
                           )


@blueprint.route('/requests/considers', methods=['GET'])
def requests_considers():
    title = 'Requests considers'
    form = RequestsForm()
    status_request = 'В обработке'
    request_list_decrypt = crypto.decrypt_all(posts.find())
    request_list_status = []
    for request_decrypt in request_list_decrypt:
        if request_decrypt['status'] == status_request:
            request_list_status.append(request_decrypt)
    return render_template('requests_considers.html',
                           page_title=title,
                           request_list=request_list_status,
                           form=form,
                           )


@blueprint.route('/requests/done', methods=['GET'])
def requests_done():
    title = 'Requests done'
    form = RequestsForm()
    status_request = 'Одобрено'
    request_list_decrypt = crypto.decrypt_all(posts.find())
    request_list_status = []
    for request_decrypt in request_list_decrypt:
        if request_decrypt['status'] == status_request:
            request_list_status.append(request_decrypt)
    return render_template('requests_done.html',
                           page_title=title,
                           request_list=request_list_status,
                           form=form,
                           )


@blueprint.route('/requests/refused', methods=['GET'])
def requests_refused():
    title = 'Requests refused'
    form = RequestsForm()
    status_request = 'Отказано'
    request_list_decrypt = crypto.decrypt_all(posts.find())
    request_list_status = []
    for request_decrypt in request_list_decrypt:
        if request_decrypt['status'] == status_request:
            request_list_status.append(request_decrypt)
    return render_template('requests_refused.html',
                           page_title=title,
                           request_list=request_list_status,
                           form=form,
                           )


@blueprint.route('/request_client/')
@blueprint.route('/request_client/<id_client>', methods=['GET', 'POST'])
def request_client(id_client):
    title = 'Client id: ' + str(id_client)
    form = Request_clientForm()
    request_list = crypto.decrypt_all(posts.find({'_id': ObjectId(id_client)}))[0]

    if request.args.get('status_request'):
        marker_change_request = request.args.get('status_request')

        if marker_change_request == 'unchanged':
            flash('You left the request without modifications.', 'secondary')
            return redirect(url_for('user.requests'))

        if marker_change_request == 'update':
            datetime_now = datetime.now()
            date_now = datetime_now.strftime('%H:%M %d.%m.%Y')
            if form.validate_on_submit():
                request_upd = {
                    '_id': ObjectId(id_client),
                    'username': form.request_list.username,
                    'service': form.request_list.service,
                    'proposal': form.request_list.proposal,
                    'status': form.request_list.status,
                    'chat_id': form.request_list.chat_id,
                    'data': {'full_name': form.request_list.data['full_name'],
                             'birthdate': '02.08.2001',
                             'birthplace': 'Город',
                             'passport_number': '7777 888888',
                             'department_code': '987-654',
                             'date_of_issue': '05.06.2006',
                             'issued_by': 'ОУФМС',
                             'address': 'Город',
                             'i_c': '123-654-987 85'
                             },
                    'date_time': '10:56 08.08.2020',
                    'date_time_upd': date_now,
                }
                request_update = []
                request_update.append(request_upd)
                request_list = crypto.encrypt_all(request_update)
                posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list[0])
                flash(f'You have successfully data update for user with id: {id_client}.', 'success')
                return render_template('request_client.html',
                                       page_title=title,
                                       id_client=id_client,
                                       form=form,
                                       request_list=request_list
                                       )
            else:
                flash('Update unsuccessful. Please check data.', 'warning')
            return render_template('request_client.html',
                                   page_title=title,
                                   id_client=id_client,
                                   form=form,
                                   request_list=request_list
                                   )

        if marker_change_request == 'done':
            status_request_done = 'Одобрено'
            request_list['status'] = status_request_done
            request_list_encrypt = []
            request_list_encrypt.append(request_list)
            request_list = crypto.encrypt_all(request_list_encrypt)
            posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list[0])
            flash(f'You have successfully change the request to DONE for user with id: {id_client}.', 'success')
            return redirect(url_for('user.requests'))

        if marker_change_request == 'refused':
            status_request_done = 'Отказано'
            request_list['status'] = status_request_done
            request_list_encrypt = []
            request_list_encrypt.append(request_list)
            request_list = crypto.encrypt_all(request_list_encrypt)
            posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list[0])
            flash(f'You have successfully change the request to REFUSED for user with id: {id_client}.', 'success')
            return redirect(url_for('user.requests'))

    return render_template('request_client.html',
                       page_title=title,
                       id_client=id_client,
                       form=form,
                       request_list=request_list
                       )








