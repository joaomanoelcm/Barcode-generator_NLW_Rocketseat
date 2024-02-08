from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json) # pega o http
    response = tag_creator_view.validate_and_create(http_request) # joga o http na view
    # será a classe HttpResponse(status_code, body)

    return jsonify(response.body), response.status_code # retornno da rota
