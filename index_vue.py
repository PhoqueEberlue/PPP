#!/usr/bin/python3
# =====================
# NOM : SAVOURÉ Florian
# ====================
from jinja2 import Environment, FileSystemLoader # ne pas modifier

# Ajouter ici les éléments du modèles dont on a besoin
from ppp_modele import *

# ne modifiez pas cette fonction !
def creer_html(fichier_template, fichier_sortie,**infos):
    """
    Cette fonction génère automatiquement un fichier à partir d'un
    template et d'informations
    paramètres :
        fichier_template : un fichier template (template HTML par exemple)
        fichier_sortie : le nom du fichier généré
        **infos : un nombre indéfini de paramètres qu'il suffit de nommer
    return : -
    """
    env=Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template=env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie, 'w', encoding='utf-8')
    f.write(html)
    f.close()

# Ajouter ici les appels à la fonction creer_html

creer_html("index_template.html", "index.html", 
            infos_ecole_inge = info(dico_des_écoles),
            infos_licence_pro = info(dico_des_licences_pro),
            infos_ecoles_info = info(dico_des_ecoles_info))
