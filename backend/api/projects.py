import os
import logging
from dataclasses import dataclass
from enum import Enum

import psycopg2

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


class ProjectType(Enum):
    commercial = 'Commercial'
    feature = 'Feature'
    game = 'Game'
    software = 'Software'
    web = 'Web'


@dataclass
class ProjectItem:
    id: int
    name: str
    code: str
    imageURI: str
    type: ProjectType
    internal: bool


def get_projects():
    db_user = os.environ['DB_USER']
    db_host = os.environ['DB_HOST']
    db_secret = os.environ['DB_SECRET']

    results = []
    conn = None

    try:
        conn = psycopg2.connect(f"dbname='{db_user}' user='{db_user}' host='{db_host}' password='{db_secret}'")
        cur = conn.cursor()
        cur.execute("""
            SELECT id, name, code, image_uri, project_type, internal 
            FROM project_items
        """)
        rows = cur.fetchall()
        for row in rows:
            results.append(ProjectItem(*row))
    except psycopg2.DatabaseError:
        LOG.exception('Unable to connect to database.')
        return []
    finally:
        if conn is not None:
            conn.close()

    return results


def add_project(body):
    name = body['name']
    code = body['code']
    project_type = body['project_type']
    # image_uri = req.get('image_uri', 'NULL')
    # internal = req.get('internal', False)

    try:
        db_user = os.environ['DB_USER']
        db_host = os.environ['DB_HOST']
        db_secret = os.environ['DB_SECRET']
    except KeyError as err:
        LOG.exception('Missing env var.')
        return 'Internal Error', 500

    project_id = None
    conn = None

    try:
        conn = psycopg2.connect(f"dbname='{db_user}' user='{db_user}' host='{db_host}' password='{db_secret}'")
        cur = conn.cursor()
        cur.execute(f"""
            INSERT INTO project_items(name, code, project_type)
            VALUES('{name}', '{code}', '{project_type}')
            RETURNING id
        """)
        project_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except:
        LOG.exception('Failed to create Project entry.')
        return 'Internal Error', 500
    finally:
        if conn is not None:
            conn.close()

    return {'id': project_id}
