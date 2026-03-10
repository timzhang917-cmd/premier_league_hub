from django.conf import settings
from django.shortcuts import render
from pathlib import Path

LOGO_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

# Team details by logo filename (edit here or switch to database later)
TEAM_INFO = {
    'asenna.jpg': {
        'name': 'Arsenal',
        'intro': 'Arsenal Football Club, based in London, is one of the traditional powerhouses of the Premier League.',
        'honors': 'English league titles, FA Cup, Community Shield, and more.',
    },
    'liwupu.png': {
        'name': 'Liverpool',
        'intro': 'Liverpool FC, from Merseyside, is one of England’s most successful clubs.',
        'honors': 'UEFA Champions League, Premier League, FA Cup, League Cup, and more.',
    },
    'manc.jpg': {
        'name': 'Manchester City',
        'intro': 'Manchester City FC has become a dominant force in the Premier League and in European competition.',
        'honors': 'Premier League, FA Cup, League Cup, UEFA Champions League, and more.',
    },
    'manu.jpg': {
        'name': 'Manchester United',
        'intro': 'Manchester United FC is one of the world’s most famous and successful clubs.',
        'honors': 'UEFA Champions League, Premier League, FA Cup, and many other major honours.',
    },
    'qieerxi.jpg': {
        'name': 'Chelsea',
        'intro': 'Chelsea FC, based in London, is a leading Premier League and European side.',
        'honors': 'UEFA Champions League, Premier League, FA Cup, UEFA Europa League, and more.',
    },
    'reci.jpg': {
        'name': 'Tottenham Hotspur',
        'intro': 'Tottenham Hotspur, from North London, is a historic top-flight club.',
        'honors': 'FA Cup, League Cup, UEFA Cup / Europa League, and more.',
    },
    'shuijing.jpg': {
        'name': 'Crystal Palace',
        'intro': 'Crystal Palace FC is a London club with a strong identity and loyal support.',
        'honors': 'FA Cup runners-up, promotions to the top flight, and various cup runs.',
    },
    'weila.jpg': {
        'name': 'Aston Villa',
        'intro': 'Aston Villa FC, from Birmingham, is one of England’s oldest and most decorated clubs.',
        'honors': 'European Cup, English league titles, FA Cup, and more.',
    },
    'xihan.jpg': {
        'name': 'West Ham United',
        'intro': 'West Ham United FC is an East London club with a rich tradition and passionate fanbase.',
        'honors': 'FA Cup, European Cup Winners’ Cup, and other domestic and European honours.',
    },
}

DEFAULT_TEAM = {'name': 'Club', 'intro': 'No introduction yet. Add it in TEAM_INFO in teams/views.py using the logo filename.', 'honors': 'None'}


def index(request):
    """Teams 首页：展示 logos 及点击弹窗中的球队介绍与荣誉"""
    logos_dir = Path(settings.BASE_DIR) / 'teams' / 'static' / 'teams' / 'logos'
    logos = []
    if logos_dir.exists():
        logos = sorted(
            f.name for f in logos_dir.iterdir()
            if f.is_file() and f.suffix.lower() in LOGO_EXTENSIONS
        )
    # 用文件名的小写形式查找，避免大小写不一致导致匹配不到
    team_info_lower = {k.lower(): v for k, v in TEAM_INFO.items()}
    teams = []
    for logo in logos:
        info = team_info_lower.get(logo.lower(), DEFAULT_TEAM.copy())
        teams.append({
            'logo': logo,
            'name': info['name'],
            'intro': info['intro'],
            'honors': info['honors'],
        })
    return render(request, 'teams/index.html', {'teams': teams})
