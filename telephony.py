from os.path import dirname

from diagrams import Node


class _Telephony(Node):
    _provider = 'telephony'
    _icon_dir = dirname(__file__) + '/resources/telephony'

    fontcolor = '#2d3436'


class Fax(_Telephony):
    _icon = 'fax.png'


class VoiceMail(_Telephony):
    _icon = 'voicemail.png'


class LandLinePhone(_Telephony):
    _icon = 'landline_phone.png'


class CellPhone(_Telephony):
    _icon = 'cellphone.png'


class SmartPhone(_Telephony):
    _icon = 'smartphone.png'


class SoftPhone(_Telephony):
    _icon = 'soft_phone.png'


class Asterisk(_Telephony):
    _icon = 'asterisk.png'


class OpenSIPS(_Telephony):
    _icon = 'opensips.png'


class OpenSER(_Telephony):
    _icon = 'openser.png'


class SER(_Telephony):
    _icon = 'ser.jpg'


class OpenSIPSControlPanel(_Telephony):
    _icon = 'opensips_control_panel.png'


class SEMS(_Telephony):
    _icon = 'sems.jpeg'


class Kamailio(_Telephony):
    _icon = 'kamailio.png'


class SipXecs(_Telephony):
    _icon = 'sipxecs.png'


class SipXcom(_Telephony):
    _icon = 'sipxcom.png'


class Elastix(_Telephony):
    _icon = 'elastix.png'


class VitalPBX(_Telephony):
    _icon = 'vitalpbx.png'


class IncrediblePBX(_Telephony):
    _icon = 'incrediblepbx.png'


class FreeSWITCH(_Telephony):
    _icon = 'freeswitch.png'


class Yate(_Telephony):
    _icon = 'yate.png'


class FreePBX(_Telephony):
    _icon = 'freepbx.png'


class MikoPBX(_Telephony):
    _icon = 'mikopbx.png'


class Issabel(_Telephony):
    _icon = 'issabel.png'


class FusionPBX(_Telephony):
    _icon = 'fusionpbx.png'


class RTPEngine(_Telephony):
    _icon = 'rtpengine.png'


class RTPProxy(_Telephony):
    _icon = 'rtpproxy.png'


class MediaProxyAGP(_Telephony):
    _icon = 'mediaproxy_ag_projects.png'


class CallCenterOperator(_Telephony):
    _icon = 'operator.png'


class CommunicationTower(_Telephony):
    _icon = 'communication_tower.png'


class FreeRADIUS(_Telephony):
    _icon = 'freeradius.png'


class FreeDiameter(_Telephony):
    _icon = 'freediameter.png'


class WalkieTalkie(_Telephony):
    _icon = 'walkietalkie.png'


class Satellite(_Telephony):
    _icon = 'satellite.png'


class DishAntenna(_Telephony):
    _icon = 'dish_antenna.png'


class SipProtocol(_Telephony):
    _icon = 'sip_protocol.png'


class VideoTalking(_Telephony):
    _icon = 'video_talking.png'


class CallTalking(_Telephony):
    _icon = 'call_talking.png'


class Kurento(_Telephony):
    _icon = 'kurento.png'


class SylkSuite(_Telephony):
    _icon = 'sylksuite.png'


class YetiSwitch(_Telephony):
    _icon = 'yeti_switch.png'


class Streamco(_Telephony):
    _icon = 'streamco.png'


class SippyB2BUA(_Telephony):
    _icon = 'sippy_b2bua.png'


class SippyGoB2BUA(_Telephony):
    _icon = 'sippy_go_b2bua.png'


class RTPCluster(_Telephony):
    _icon = 'rtp_cluster.png'


class GnuBayonne(_Telephony):
    _icon = 'gnu_bayonne.jpg'


class DaloRADIUS(_Telephony):
    _icon = 'daloradius.png'


class Kazoo(_Telephony):
    _icon = 'kazoo.png'


class WazoPlatform(_Telephony):
    _icon = 'wazo_platform.png'
