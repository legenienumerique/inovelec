"""Générateur de la maquette Inov'Elec (Châtillon-sur-Chalaronne). Usage : python build.py <dossier-du-projet>
Pas de site, pas de réseau social, pas de fiche Google. Contenus relevés le 13/11/2026 :
annuaire des entreprises (création 2008, activité), Societe.com (activité déclarée : électricité générale,
installation et vente d'antennes ; gérant Pascal Grandjean), PagesJaunes (téléphone).
Aucune photo disponible : visuels graphiques (affiches et dessins au trait), sans photo de banque d'images."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 1  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '06 84 62 38 89', 'tel:0684623889'
ADR = ('334 chemin de Thiboloup', '01400 Châtillon-sur-Chalaronne')
NAV = [('prestations.html', 'Prestations')]


def pill(t, href, cls='', arrow='↗', ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="pill {cls}" href="{href}"{x}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def im(k):
    return f'{PH}{k}.svg'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><i class="bulb"></i><span><span class="wm">Inov’<i>Elec</i></span><small>Électricité générale</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('devis.html', 'Devis gratuit', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#16171b">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{im('ampoule')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Inov’Elec, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Électricien à Châtillon-sur-Chalaronne depuis 2008. Électricité générale, installation et vente d’antennes.</p></div>
<div><h4 class="micro">Inov’Elec</h4><ul><li><a href="prestations.html">Électricité générale</a></li><li><a href="prestations.html#antennes">Antennes</a></li><li><a href="devis.html">Demander un devis</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="devis.html">Formulaire de devis</a></li></ul></div>
<div><h4 class="micro">Nous trouver</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">INOV’ELEC</div>
<div class="fb micro"><span class="pad">© Inov’Elec</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Un projet, <em>une panne ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Devis gratuit</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Demander un devis', 'devis.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


PREST = [('Électricité générale', 'Installation électrique dans tous locaux : maison, appartement, local professionnel.', 'tableau'),
         ('Antennes', 'Installation et vente d’antennes : la bonne réception, chez vous.', 'antenne'),
         ('Dépannage', 'Une panne, un disjoncteur qui saute : un appel au 06 84 62 38 89.', 'prise'),
         ('Rénovation', 'Remettre une installation à neuf, pièce par pièce.', 'ampoule')]


def pages():
    P = {}
    hero_tiles = [('t1', 'tableau'), ('t2', 'ampoule'), ('t3', 'volt'), ('t4', 'antenne'), ('t5', 'prise'), ('t6', 'cable'), ('t7', 'annee')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{im(f)}" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(im(f)) for f in ['tableau', 'ampoule', 'antenne', 'prise', 'volt', 'cable', 'annee', 'ville'])
    wall_imgs = ['tableau', 'ampoule', 'volt', 'antenne', 'prise', 'cable', 'annee', 'ville', 'tel']
    wall = ''.join(tile(im(wall_imgs[i % len(wall_imgs)])) for i in range(54))
    items = [('prestations.html', '01', 'Électricité', 'Installation électrique dans tous locaux.', 'tableau', 'Générale'),
             ('prestations.html#antennes', '02', 'Antennes', 'Installation et vente d’antennes.', 'antenne', 'Réception'),
             ('devis.html', '03', 'Dépannage', 'Un appel, on vous rappelle.', 'prise', 'Sur appel'),
             ('devis.html', '04', 'Devis', 'Gratuit, sans engagement.', 'tel', 'Gratuit')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>{b}</b></span></a>' for h, n, t, d, _, b in items)
    prev = ''.join(tile(im(it[4]), 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{im(f)}" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [
        ('tableau', 'Tableau électrique'), ('prise', 'Prises et circuits'), ('ampoule', 'Éclairage'), ('antenne', 'Antennes'), ('cable', 'Câblage'), ('volt', 'Mise en service')])
    steps = [('Vous appelez', f'Au {TEL}, ou par le formulaire.'),
             ('Vous expliquez', 'Votre projet ou votre panne.'),
             ('Vous recevez le devis', 'Clair, gratuit, sans engagement.'),
             ('On intervient', 'Chez vous, à Châtillon et alentours.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Électricité générale', 'Antennes', 'Dépannage', 'Rénovation', 'Devis gratuit', 'Depuis 2008'] * 2)

    P['index.html'] = head('Inov’Elec — Électricien à Châtillon-sur-Chalaronne depuis 2008', 'Inov’Elec, électricien à Châtillon-sur-Chalaronne depuis 2008 : électricité générale, installation et vente d’antennes. Devis gratuit au 06 84 62 38 89.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Électricien</b>depuis 2008</div>
<div class="cap micro c2"><b>Électricité générale</b>antennes</div>
<div class="cap micro c3"><b>Châtillon-sur-Chalaronne</b>et alentours</div>
<div class="go">{pill('Devis gratuit', 'devis.html')}</div>
{ht}
<p class="para">Votre électricien, à Châtillon-sur-Chalaronne.</p>
<h1 class="word">INOV’ELEC</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Bienvenue</span><h2 class="sp">Le courant <em>passe</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Depuis 2008, Inov’Elec réalise vos travaux d’électricité à Châtillon-sur-Chalaronne : installation électrique dans tous locaux, installation et vente d’antennes.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Depuis 2008</b>, entreprise de Châtillon-sur-Chalaronne.</span></li><li><span><b>Pascal Grandjean</b>, gérant depuis 2008.</span></li><li><span><b>Devis gratuit</b>, sur simple appel.</span></li></ul>{pill('Nos prestations', 'prestations.html', 'blue')}</div>{tile(im('ville'), '', par=8, alt='Électricien à Châtillon-sur-Chalaronne')}</div></section>

<section class="story"><span class="micro mute m3">Notre métier</span>
<h2><span class="w">Une</span> <span class="w">installation</span> <span class="w">sûre,</span> <span class="w">du</span> <span class="w">tableau</span> <span class="w">à</span> <span class="w"><em>l’antenne</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Électricité générale et antennes.</p><span class="micro mute m2">Depuis 2008</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Devis gratuit</span><h2>On <em>branche</em> quoi ?</h2>{pill('Demander un devis', 'devis.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos prestations</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Que pouvons-nous <em>faire ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Du sol au toit</span><h2>Toute votre <em>installation</em></h2></div>{pill('Prestations', 'prestations.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">En chiffres</span><h2 class="sp">Une entreprise <em>d’ici</em></h2>
<div class="cnt rv"><div><b data-to="2008">0</b><span>année de création, à Châtillon-sur-Chalaronne</span></div><div><b data-to="18">0</b><span>ans d’expérience</span></div><div><b data-to="1">0</b><span>numéro pour tout : le {TEL}</span></div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Comment ça marche</span><h2 class="sp">Simple <em>comme un interrupteur</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    rows = ''.join(f'<section class="sec"{" id=antennes" if k == "antenne" else ""} style="padding-top:{"0" if i else ""}"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">0{i + 1}</span><h2 class="sp">{t}</h2><p class="lead rv" style="margin-top:1.4rem">{d}</p></div>{tile(im(k), "", par=8, alt=t)}</div></section>' for i, (t, d, k) in enumerate(PREST))
    P['prestations.html'] = head('Prestations — Inov’Elec, électricien à Châtillon-sur-Chalaronne', 'Électricité générale, installation et vente d’antennes, dépannage et rénovation électrique à Châtillon-sur-Chalaronne. Devis gratuit.', 'prestations.html') + pagehead('Prestations', 'Du tableau <em>à l’antenne</em>', 'Électricité générale dans tous locaux, installation et vente d’antennes. Un artisan de Châtillon-sur-Chalaronne, depuis 2008.', im('tableau'), im('antenne')) + rows + '''
<section class="sec" style="padding-top:0"><div class="wrap"><p class="note">Liste des prestations à confirmer avec Inov’Elec.</p></div></section>''' + cta() + foot()

    P['devis.html'] = head('Devis gratuit — Inov’Elec, électricien à Châtillon-sur-Chalaronne', f'Demandez votre devis gratuit à Inov’Elec, électricien à Châtillon-sur-Chalaronne : {TEL}.', 'devis.html') + pagehead('Devis', 'Votre devis, <em>gratuit</em>', 'Décrivez votre projet ou votre panne en quelques mots : Inov’Elec vous rappelle.', im('tel')) + f'''
<section class="sec" id="devis"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Contact</span><h2 class="sp">Un appel <em>suffit</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Le plus simple : appelez le <a href="{TELH}">{TEL}</a>. Ou laissez votre message, on vous rappelle.</p>
<div class="hor rv"><span><b>Téléphone</b> · <a href="{TELH}">{TEL}</a></span><span><b>Adresse</b> · {ADR[0]}, {ADR[1]}</span><span class="micro">Horaires et zone d’intervention à confirmer avec Inov’Elec</span></div></div>
<form class="f rv" id="dv"><div class="seg"><button type="button" class="on">Travaux</button><button type="button">Antenne</button><button type="button">Dépannage</button></div>
<div class="r2"><div class="fld"><label for="dn">Nom</label><input id="dn" required></div><div class="fld"><label for="dt">Téléphone</label><input id="dt" type="tel" required></div></div>
<div class="fld"><label for="dc">Commune</label><input id="dc" placeholder="Châtillon-sur-Chalaronne"></div>
<div class="fld"><label for="dm">Votre projet</label><textarea id="dm" rows="4" placeholder="Tableau à changer, prises à ajouter, antenne…"></textarea></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun message n’est envoyé.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
