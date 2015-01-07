<html>
<head>
<link rel="stylesheet" href="${request.static_url('changelog:static/changelog.css')}" type="text/css"/>
<link rel="stylesheet" href="${request.static_url('changelog:static/deform/css/form.css')}" type="text/css"/>
<script type="text/javascript" src="${request.static_url('changelog:static/deform/scripts/jquery-1.4.2.min.js')}"></script>
<script type="text/javascript" src="${request.static_url('changelog:static/deform/scripts/deform.js')}"></script>
<link rel="shortcut icon" href="${request.static_url('changelog:static/favicon.png')}">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>

</head>
<body>
<%
  from velruse import login_url
  logged_in=request.user
  loginurl=login_url(request, 'google')
  logouturl=request.route_url('logout')
%>
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
<div class="container">
       <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Changelog</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="${request.route_url('AddEntry')}">Add Entry</a></li>
% if logged_in is not None:
            <li><a href="${logouturl}">Logout</a></li>
% else:
            <li><a href="${loginurl}">Login</a></li>
% endif
          </ul>
        </div><!--/.nav-collapse -->

</div>
</nav>

<div class="container">
<%block name="BlockContent"/>
</div>
</body>
</html>
