<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>EPIC EVENT</h1>
	<p>
		Epic Events est une entreprise de conseil et de gestion dans l'événemenentiel qui 
		répond aux besoins des start-up voulant des <<fêtes épiques>>.
		Retrouvez dans ce repository le logiciel de gestion relation client (CRM) de l'entreprise, 
		qui effectue le suivide tous les clients et événemenets.
	</p>
	<h2>Installtion</h2>
	<p>
		<ul>
			<li>Clonez le repository <code>git clone</code></li>
			<li>Se déplacer dans le répertoire racine epic-events <code>cd epic-events</code></li>
			<li>Créer un environnement virtuel <code>python -m venv env</code></li>
			<li>Activez l'environnement virtuel <code>env\Scripts\activate.bat</code></li>
			<li>Installez les dépendances du project <code>pip install -r requirements.txt</code></li>
		</ul>
	</p>
	<h3>Documentation API</h3>
	</p>
	<table>
		<tr>
			<th>Point de terminaison d'API</th>
			<th>Méthode HTTP</th>
			<th>URI</th>
		</tr>
		<tr>
			<td>Connexion de l'utilisateur</td>
			<td>POST</td>
			<td>/login/</td>
		</tr>
		<tr>
			<td>Récupérer la liste de tous les clients</td>
			<td>GET</td>
			<td>/client/</td>
		</tr>
		<tr>
			<td>Ajouter un client</td>
			<td>POST</td>
			<td>/client/</td>
		</tr>
		<tr>
			<td>Récupérer plus d'informations sur un  client</td>
			<td>GET</td>
			<td>/client/{id}/</td>
		</tr>
		<tr>
			<td>Mettre à jour les informations d'un client</td>
			<td>PUT</td>
			<td>/client/{id}/</td>
		</tr>
		<tr>
			<td>Supprimer un client et ses événements</td>
			<td>DELETE</td>
			<td>/client/{id}/</td>
		</tr>
		<tr>
			<td>Récupérer la liste de tous les utilisateurs du CRM</td>
			<td>GET</td>
			<td>/users/</td>
		</tr>
		<tr>
			<td>Ajouter un utilisateur au CRM</td>
			<td>POST</td>
			<td>/users/</td>
		</tr>
		<tr>
			<td>Récupérer les détails sur un utilisateur</td>
			<td>GET</td>
			<td>/users/{id}</td>
		</tr>
		<tr>
			<td>Actualiser les informations d'un utilisateur</td>
			<td>PUT</td>
			<td>/users/{id}</td>
		</tr>
		<tr>
			<td>Supprimer un utilisateur</td>
			<td>DELETE</td>
			<td>/users/{id}</td>
		</tr>
		<tr>
			<td>Récupérer la liste des événements</td>
			<td>GET</td>
			<td>/events/{id}</td>
		</tr>
		<tr>
			<td>Créer un événement</td>
			<td>POST</td>
			<td>/event/</td>
		</tr>
		<tr>
			<td>Récuperer lrs détails d'un événement</td>
			<td>GET</td>
			<td>/event/{id}</td>
		</tr>
		<tr>
			<td>Mettre à jour un événement</td>
			<td>PUT</td>
			<td>/event/{id}</td>
		</tr>
		<tr>
			<td>Supprimer un événement</td>
			<td>DELETE</td>
			<td>/event/{id}/</td>
		</tr>
		<tr>
			<td>Créer un contrat</td>
			<td>POST</td>
			<td>/contract/</td>
		</tr>
		<tr>
			<td>Récupérer la liste des contrats</td>
			<td>GET</td>
			<td>/contract/</td>
		</tr>
		<tr>
			<td>Mettre à jour un contract</td>
			<td>PUT</td>
			<td>/contract/{id}/</td>
		</tr>
		<tr>
			<td>Supprimer un contract</td>
			<td>DELETE</td>
			<td>/contract/{id}/</td>
		</tr>
		<tr>
			<td>Récupérer un contract via son id</td>
			<td>GET</td>
			<td>/contract/{id}/</td>
		</tr>
	</table>
</body>
</html>