import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

wallpaper_folder = "/usr/share/backgrounds"
wallpaper_file = "System76-Robot-by_Kate_Hazen_of_System76.png"
wallpaper_path = "%s/%s" % (wallpaper_folder, wallpaper_file)


def test_system76_driver_package(host):
    assert host.package("system76-driver").is_installed


def test_system76_wallpapers_package(host):
    assert host.package("system76-wallpapers").is_installed


def test_system76_default_wallpaper_exists(host):
    wallpaper = host.file(wallpaper_path)

    assert wallpaper.exists
    assert wallpaper.is_file


def test_system76_default_wallpaper_set(host):
    schema = "org.gnome.desktop.background"
    key = "picture-uri"
    setting = host.run("gsettings get %s %s" % (schema, key))

    assert setting.stdout == "'file://%s'" % wallpaper_path
