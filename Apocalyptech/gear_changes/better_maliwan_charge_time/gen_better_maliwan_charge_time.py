#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

scale_pistol = 0.5
scale_shotgun = 0.4
scale_smg = 0.5
scale_sniper = 0
scale_heavy = 0.5

mod = Mod('better_maliwan_charge_time.bl3hotfix',
        'Better Maliwan Charge Time',
        'Apocalyptech',
        [
            'Reduces the charge time for Maliwan guns.',
            '',
            "Note that it's possible that any gun whose damage depends on charge time could",
            '*possibly* be nerfed by this, if the damage is based on time and not charge',
            "percent.  I think they're probably fine but have not tested it.",
            '',
            'Pistol Scaling: {:d}%'.format(int(scale_pistol*100)),
            'Shotgun Scaling: {:d}%'.format(int(scale_shotgun*100)),
            'SMG Scaling: {:d}%'.format(int(scale_smg*100)),
            'Sniper Scaling: {:d}%'.format(int(scale_sniper*100)),
            #'',
            #"Also (possibly) buffs the charge time for the ION CANNON, even though it's a Vladof gun.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.3.0',
        cats='gear-brand, cheat',
        )

def charge_time(mod,
        obj_name,
        new_val,
        final_attr='ChargeTime',
        prev_val=None,
        aspect_list=1,
        aspect_obj='AspectList_WeaponUseModeSecondaryAspectData',
        aspect_attr='Component_BPWeaponChargeComponent_MAL',
        ):
    if prev_val is None:
        prev_val = ''
    else:
        prev_val = '(BaseValue={:.6f})'.format(prev_val)
    mod.reg_hotfix(Mod.PATCH, '',
            '{}:{}.{}'.format(Mod.get_full_cond(obj_name), aspect_obj, aspect_attr),
            'AspectList.AspectList[{}].Object..Component.Object..{}'.format(aspect_list, final_attr),
            '(BaseValue={:.6f})'.format(new_val),
            prev_val=prev_val)

# Put in our improvements
mod.header('Generic Weapons')
for (label, obj_name, aspect_num, default, scale, aspect_obj) in [
        ('Pistol: Atomizer',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_PS_MAL_Barrel_01',
            2,
            0.5,
            scale_pistol,
            'WeaponUseModeSecondaryAspectData_0'),
        ('Pistol: Melter',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_PS_MAL_Barrel_02',
            2,
            1,
            scale_pistol,
            'WeaponUseModeSecondaryAspectData_1'),
        ('Pistol: Blaster',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_PS_MAL_Barrel_03.Part_PS_MAL_Barrel_03',
            0,
            0.7,
            scale_pistol,
            None),
        ('Shotgun: Terminator',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_MAL_Barrel_01.Part_SG_MAL_Barrel_01',
            1,
            0.7,
            scale_shotgun,
            None),
        ('Shotgun: Shockwave',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SG_MAL_Barrel_02.Part_SG_MAL_Barrel_02',
            1,
            1.05,
            scale_shotgun,
            None),
        ('Shotgun: Cyclotron',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SG_MAL_Barrel_03.Part_SG_MAL_Barrel_03',
            1,
            0.9,
            scale_shotgun,
            None),
        ('SMG: Pulsar',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SM_MAL_Barrel_01.Part_SM_MAL_Barrel_01',
            1,
            0.75,
            scale_smg,
            None),
        ('SMG: Nebula',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_02/Part_SM_MAL_Barrel_02.Part_SM_MAL_Barrel_02',
            1,
            0.85,
            scale_smg,
            None),
        ('SMG: Quasar',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Barrel/Barrel_03/Part_SM_MAL_Barrel_03.Part_SM_MAL_Barrel_03',
            1,
            1.0,
            scale_smg,
            None),
        ('Sniper Rifle: Multiplex',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_01/Part_MAL_SR_Barrel_01.Part_MAL_SR_Barrel_01',
            1,
            1.1,
            scale_sniper,
            None),
        ('Sniper Rifle: Particle Rifle',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_02/Part_MAL_SR_Barrel_02.Part_MAL_SR_Barrel_02',
            1,
            0.9,
            scale_sniper,
            None),
        ('Sniper Rifle: Proton Rifle',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Parts/Barrel/Barrel_03/Part_MAL_SR_Barrel_03.Part_MAL_SR_Barrel_03',
            1,
            1.75,
            scale_sniper,
            None),
        ]:

    if not aspect_obj:
        aspect_obj = 'AspectList_WeaponUseModeSecondaryAspectData'

    mod.comment('{} (default: {})'.format(label, default))
    charge_time(mod, obj_name, default*scale,
            aspect_obj=aspect_obj,
            aspect_list=aspect_num,
            )
    mod.newline()

mod.header('Legendaries/Uniques')
for label, obj_name, default, scale, aspect_obj, aspect_num, aspect_attr, final_attr in [
        ('Beacon',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Parts/Part_PS_MAL_Barrel_Decoupler',
            0.7,
            scale_pistol,
            None,
            None,
            None,
            None),
        ('Binary Operator',
            '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Parts/Part_MAL_SR_Barrel_BinaryOperator',
            1,
            scale_sniper,
            None,
            2,
            None,
            None),
        ('Blind Bandit',
            '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Parts/Part_SG_MAL_Barrel_BlindBandit_Epic',
            1.05,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Blind Sage',
            '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Parts/Part_SG_MAL_Barrel_BlindBandit',
            1.05,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Bubble Blaster',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Parts/Part_PS_MAL_Barrel_BubbleBlaster',
            0.5,
            scale_pistol,
            'WeaponUseModeSecondaryAspectData_0',
            None,
            None,
            None),
        ('Chandelier',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Parts/Part_SG_MAL_Barrel_Antler',
            1.05,
            scale_shotgun,
            None,
            None,
            'BPWeaponChargeComponent_MAL_C_0',
            None),
        ('Cloud Kill',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Parts/Part_SM_MAL_Barrel_CloudKill.Part_SM_MAL_Barrel_CloudKill',
            0.8,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Complex Root',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Parts/Part_MAL_SR_Barrel_ImaginaryNumber',
            # The default `ChargeTime` is 1, which is why this value doesn't show up in serializations.
            1,
            scale_sniper,
            None,
            None,
            None,
            None),
        ('Crit',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Parts/Part_SM_MAL_Barrel_Crit.Part_SM_MAL_Barrel_Crit',
            0.75,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Cutsman',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Parts/Part_SM_MAL_Barrel_Cutsman.Part_SM_MAL_Barrel_Cutsman',
            1.0,
            scale_smg,
            None,
            None,
            None,
            None),
        ('D.N.A.',
            '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Parts/Part_SM_MAL_Barrel_DNA',
            # The `ChargeTime` attr is 1.0, which won't show up in serializations 'cause that's the default.
            # You can see it with `getall`, though.
            1.0,
            scale_smg,
            None,
            3,
            None,
            None),
        ('Destructo Spinner',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Part/Part_SM_MAL_Barrel_DestructoSpin.Part_SM_MAL_Barrel_DestructoSpin',
            0.5,
            scale_smg,
            None,
            None,
            None,
            None),
        ('E-Gone',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Parts/Part_SM_MAL_Barrel_Egon.Part_SM_MAL_Barrel_Egon',
            0.85,
            scale_smg,
            None,
            None,
            None,
            None),
        ("Ember's Purge",
            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Parts/Part_SM_MAL_Barrel_EmbersPurge.Part_SM_MAL_Barrel_EmbersPurge',
            0.75,
            scale_smg,
            None,
            None,
            None,
            None),
        ("The Emperor's Condiment",
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Parts/Part_SM_MAL_Barrel_Emporer.Part_SM_MAL_Barrel_Emporer',
            0.85,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Firestorm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_FireStorm.Part_MAL_SR_Barrel_FireStorm',
            1.0, # pre-GBX-hotfix value: 1.75
            scale_sniper,
            None,
            None,
            None,
            None),
        ('Flipper',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Parts/Part_SM_MAL_Barrel_Flipper',
            0.85,
            scale_smg,
            'WeaponUseModeSecondaryAspectData_0',
            None,
            None,
            None),
        ('Free Radical',
            '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Deatomizer/Parts/Part_PS_MAL_Barrel_Deatomizer2',
            # Okay, fun!  When the `ChargeTime` attr isn't in the serializations, it's 'cause it's
            # set to the default of 1.0.  You can see it with a `getall`.
            1.0,
            scale_pistol,
            None,
            0,
            None,
            None),
        ('Frequency',
            '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Parts/Part_SG_MAL_Barrel_Frequency',
            1.05,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Hellshock',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Parts/Part_PS_MAL_Barrel_HellShock.Part_PS_MAL_Barrel_HellShock',
            0.8,
            scale_pistol,
            None,
            None,
            None,
            None),
        ('Ice Pick',
            '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Parts/Part_PS_MAL_Barrel_IcePick',
            1,
            scale_pistol,
            'WeaponUseModeSecondaryAspectData_1',
            2,
            None,
            None),
        ('ION LASER',
            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Parts/Part_SM_MAL_Barrel_IonLaser.Part_SM_MAL_Barrel_IonLaser',
            0.45,
            scale_smg,
            None,
            None,
            None,
            None),
        ("Kill-o'-the-Wisp",
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Parts/Part_SG_MAL_Barrel_Wisp.Part_SG_MAL_Barrel_Wisp',
            1.0,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Krakatoa',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Parts/Part_MAL_SR_Barrel_Krakatoa.Part_MAL_SR_Barrel_Krakatoa',
            1.0,
            scale_sniper,
            None,
            None,
            None,
            None),
        ("Kyb's Worth",
            '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Parts/Part_SM_MAL_Barrel_KybsWorth.Part_SM_MAL_Barrel_KybsWorth',
            0.85,
            scale_smg,
            None,
            None,
            None,
            None),
        ("Miss Moxxi's Vibra-Pulse",
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Parts/Part_SM_MAL_Barrel_VibraPulse.Part_SM_MAL_Barrel_VibraPulse',
            1.15,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Nothingness',
            '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Parts/Part_SG_MAL_Barrel_TheNothing',
            1.05,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('P2P Networker',
            '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Parts/Part_SM_MAL_Barrel_Link.Part_SM_MAL_Barrel_Link',
            0.85,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Projectile Recursion',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Parts/Part_SG_MAL_Barrel_Recursion.Part_SG_MAL_Barrel_Recursion',
            1.0,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Shrieking Devil',
            '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Parts/Part_SG_MAL_Barrel_Shriek.Part_SG_MAL_Barrel_Shriek',
            2.0,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ('Soleki Protocol',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Parts/Part_MAL_SR_Barrel_Soleki.Part_MAL_SR_Barrel_Soleki',
            1.25,
            scale_sniper,
            None,
            None,
            None,
            None),
        ('Starkiller',
            '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Parts/Part_PS_MAL_Barrel_Starkiller',
            1,
            scale_pistol,
            'WeaponUseModeSecondaryAspectData_1',
            2,
            None,
            None),
        ('Storm',
            '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Parts/Part_MAL_SR_Barrel_Storm.Part_MAL_SR_Barrel_Storm',
            1.0, # pre-GBX-hotfix value: 2.0
            scale_sniper,
            None,
            None,
            None,
            None),
        ('Superconducting Plasma Coil',
            '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Parts/Part_SM_MAL_Barrel_PlasmaCoil',
            0.5,
            scale_smg,
            None,
            None,
            None,
            None),
        ('Tsunami',
            '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Parts/Part_SM_MAL_Barrel_Tsunami.Part_SM_MAL_Barrel_Tsunami',
            0.8,
            scale_smg,
            None,
            None,
            None,
            None),
        ("Vosk's Deathgrip",
            '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Parts/Part_SG_MAL_Barrel_DeathGrip.Part_SG_MAL_Barrel_DeathGrip',
            0.9,
            scale_shotgun,
            None,
            None,
            None,
            None),
        ]:
    if not aspect_obj:
        aspect_obj = 'AspectList_WeaponUseModeSecondaryAspectData'
    if not aspect_attr:
        aspect_attr = 'Component_BPWeaponChargeComponent_MAL'
    if not final_attr:
        final_attr = 'ChargeTime'
    if aspect_num is None:
        aspect_num = 1
    mod.comment('{} (default: {})'.format(label, default))
    charge_time(mod,
            obj_name,
            default*scale,
            aspect_obj=aspect_obj,
            aspect_attr=aspect_attr,
            final_attr=final_attr,
            aspect_list=aspect_num,
            )
    mod.newline()

# This doesn't seem to actually do the trick, and I don't care enough to track
# it down.  Was technically out-of-place anyway.
# TODO: Plaguebearer? (Torgue HW)
#mod.header('Non-Maliwan Weapons')
#for label, obj_name, aspect_attr, aspect_idx, default, scale in [
#        ('ION CANNON (Vladof Heavy Weapon)',
#            '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Parts/Part_HW_VLA_Barrel_IonCannon.Part_HW_VLA_Barrel_IonCannon',
#            'Component_WeaponChargeComponent',
#            7,
#            2,
#            scale_heavy),
#        ]:
#    mod.comment('{} (default: {})'.format(label, default))
#    charge_time(mod, obj_name, default*scale, aspect_list=aspect_idx, aspect_attr=aspect_attr)
#    mod.newline()

mod.close()
