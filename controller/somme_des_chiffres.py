from flask import Flask, request, Response, Blueprint

sum_way = Blueprint('somme_des_chiffres', __name__)


# Calcul de la somme des chiffres d'un sombre
def sum_didgit(number: int) -> int:
    return sum(int(digit) for digit in str(number))


# Outil de conversion de la response serveur en XML
def dict_to_xml(tag, d):
    parts = [f'<{tag}>']
    for key, val in d.items():
        parts.append(f'<{key}>{val}</{key}>')
    parts.append(f'</{tag}>')
    return ''.join(parts)


# Route pour calculer la somme des chiffres
# et retourner le résultat en XML
# http://localhost:5000/sum_didgit?number=123

@sum_way.route('/sum_didgit', methods=['GET'])
def request_sum_of_didgit():
    number = request.args.get('number', default=0, type=int)
    if number < 0:
        xml_response = dict_to_xml('erreur', {'message': 'le nombre doit être positif'})
        return Response(xml_response, mimetype='application/xml'), 400
    else:
        result = sum_didgit(number)
        xml_response = dict_to_xml('response', {'number': number, ' Sum_of_Didgit': result})
        return Response(xml_response, mimetype="application/xml")
