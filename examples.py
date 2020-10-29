from diagrams import Diagram, Cluster

from telephony import *

with Diagram('Examples', show=False, direction='TB'):
    with Cluster('VoIP'):
        with Cluster('Media Servers'):
            kurento = Kurento('Kurento')
            sems = SEMS('SEMS')

        with Cluster('Media Proxies'):
            rtpproxy = RTPProxy('RTPProxy')
            rtpengine = RTPEngine('RTPEngine')
            rtp_cluster = RTPCluster('RTPCluster')
            mediaproxy_agp = MediaProxyAGP('MediaProxy\nby AG Projects')

        with Cluster('AAA Servers'):
            freeradius = FreeRADIUS('FreeRADIUS')
            freediameter = FreeDiameter('FreeDiameter')

            with Cluster('UI'):
                daloradius = DaloRADIUS('daloRADIUS')
                daloradius >> freeradius

        with Cluster('SoftSwitches'):
            yeti_switch = YetiSwitch('Yeti')

            yeti_switch >> sems

            streamco = Streamco('Streamco')

            freeswitch = FreeSWITCH('FreeSWITCH')

        with Cluster('Telephony platform'):
            wazo = WazoPlatform('Wazo')
            kazoo = Kazoo('Kazoo')

        with Cluster('Telephony engines'):
            asterisk = Asterisk('Asterisk')
            opensips = OpenSIPS('OpenSIPS')
            openser = OpenSER('OpenSER')
            kamailio = Kamailio('Kamailio')
            yate = Yate('Yate')
            sipxecs = SipXecs('SipXecs')
            ser = SER('SIP Express Router (SER)')
            sippy_b2bua = SippyB2BUA('Sippy B2BUA')
            sippy_go_b2bua = SippyGoB2BUA('Sippy Go B2BUA')
            gnu_bayonne = GnuBayonne('GNU Bayonne')

            sipxecs >> freeswitch
            streamco >> asterisk

            with Cluster('Unified Communications Server'):
                sylksuite = SylkSuite('Sylk Suite')

                sipxcom = SipXcom('SipXcom')

                issabel = Issabel('Issabel')
                issabel >> asterisk

                elastix = Elastix('Elastix')
                elastix >> asterisk

        wazo >> asterisk
        kazoo >> freeswitch
        kazoo >> kamailio

        with Cluster('Control Panels'):
            opensips_cp = OpenSIPSControlPanel('OpenSIPS\nControl Panel')

            opensips >> opensips_cp

        with Cluster('PBX systems'):
            freepbx = FreePBX('FreePBX')
            freepbx >> asterisk
            elastix >> freepbx

            mikopbx = MikoPBX('MikoPBX')
            mikopbx >> asterisk

            vitalpbx = VitalPBX('VitalPBX')
            vitalpbx >> asterisk

            incrediblepbx = IncrediblePBX('IncrediblePBX')
            incrediblepbx >> asterisk

            fusionpbx = FusionPBX('FusionPBX')
            fusionpbx >> freeswitch

    with Cluster('Communication devices'):
        soft_phone = SoftPhone('SoftPhone')
        cellphone = CellPhone('CellPhone')
        smartphone = SmartPhone('SmartPhone')
        landline_phone = LandLinePhone('LandLinePhone')

        fax = Fax('Fax')

    with Cluster('Other'):
        satellite = Satellite('Satellite')
        dish_antenna = DishAntenna('DishAntenna')

        satellite >> dish_antenna

        sip_protocol = SipProtocol('SipProtocol')

        walkie_talkie = WalkieTalkie('WalkieTalkie')
        communication_tower = CommunicationTower('CommunicationTower')
        call_center_operator = CallCenterOperator('CallCenterOperator')

        voicemail = VoiceMail('VoiceMail')

        call_talking = CallTalking('CallTalking')

        person_1 = VideoTalking('VideoTalking')
        person_2 = VideoTalking('VideoTalking')

        person_1 >> sip_protocol >> person_2
        person_2 >> sip_protocol >> person_1
