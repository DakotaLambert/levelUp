"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game
from levelupreports.views import Connection


def userevent_list(request):
    """[summary]

    Args:
        request ([type]): [description]
    """
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT 
                    g.id,
                    u.first_name || " " || u.last_name as full_name,
                    e.id,
                    e.date,
                    e.time,
                    gm.name

                    FROM levelupapi_event e
                    JOIN levelupapi_eventgamer eg
                        ON e.id = eg.event_id
                    JOIN levelupapi_gamer g
                        ON g.id = eg.gamer_id
                    JOIN auth_user
                        ON u.id = g.user_id
                    JOIN levelupapi_game gm
                        ON e.game_id = gm.id
            """)
