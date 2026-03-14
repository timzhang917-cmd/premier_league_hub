from django.db import migrations


def ensure_created_at_column(apps, schema_editor):
    table_name = "teams_team"
    connection = schema_editor.connection

    with connection.cursor() as cursor:
        columns = {
            column.name
            for column in connection.introspection.get_table_description(cursor, table_name)
        }

    if "created_at" not in columns:
        schema_editor.execute(
            "ALTER TABLE teams_team ADD COLUMN created_at datetime NULL"
        )
        schema_editor.execute(
            "UPDATE teams_team SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL"
        )


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0003_seed_forum_teams"),
    ]

    operations = [
        migrations.RunPython(ensure_created_at_column, migrations.RunPython.noop),
    ]
