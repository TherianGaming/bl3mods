#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('expanded_pt1_scaling.txt',
        'Expanded PT1 Scaling',
        [
            "NOTE: This doesn't actually *work*, alas.  The object gets updated",
            "properly but nothing changes in-game.  Pff.",
            "",
            "Removes the MaxGameStage bound on all the zones in the main game",
            "during Playthrough 1/Normal (the MaxGameStages for all DLC so far is",
            "already effectively unlocked), so areas should be able to scale as",
            "high as the player.  This should theoretically remove issues such as",
            "the sudden down-scaling in Splinterlands, for instance.  It will also",
            "allow the endgame levels to scale all the way up to 50 -- a full",
            "Normal runthrough will probably leave your character at 50.",
            ""
            "Note that there appears to be some cross-contamination of zones and",
            "levels, so it's possible that these changes aren't applying fully in",
            "all cases.  This is currently untested, I'll have to go through a",
            "playthrough to find out if it's doing the right thing.",
        ],
        'ExpandedPT1Scale',
        )

# For a version which *basically* does what I want here, see the working
# nvhm_gamestage_follows_level.txt in the parent dir.  That's a bit more aggressive
# than what I tried here, but since what I tried here didn't *work*, I'll just
# take what I can get.

# Code generated by gen.py in my own data extraction dir, in /Game/GameData/Regions
# There appears to be a number of cases where these regions are used outside the
# levels which match the region names; I've used code and my BL3 Refs database to
# theoretically catch all of those cases.
for r_name, r_idx, levels, num_missions in [
        ('Region_Sanctuary', 0,
            ['Sanctuary3_P'],
            0),
        ('Region_Zone0_Recruitment_A', 1,
            ['Desert_P', 'Outskirts_P', 'Recruitment_P', 'Sanctuary3_P'],
            0),
        ('Region_Zone0_Recruitment_B', 2,
            ['CityVault_P', 'Recruitment_P', 'Sacrifice_P'],
            0),
        ('Region_Zone0_Prologue_A', 3,
            ['Desert_P', 'Prologue_P'],
            0),
        ('Region_Zone0_Prologue_B', 4,
            ['Prologue_P', 'Recruitment_P'],
            0),
        ('Region_Zone0_Prologue_C', 5,
            ['Prologue_P'],
            0),
        ('Region_Zone0_Prologue_E', 6,
            ['Prologue_P'],
            0),
        ('Region_Zone0_Prologue_Skagzilla', 7,
            ['Prologue_P'],
            0),
        ('Region_Zone0_Prologue_F', 8,
            ['Prologue_P'],
            0),
        ('Region_Zone0_Sacrifice_A', 9,
            ['CityVault_P', 'City_P', 'Sacrifice_P'],
            1),
        ('Region_Zone0_Sacrifice_B', 10,
            ['Sacrifice_P'],
            1),
        ('Region_Zone0_Sacrifice_Moutpiece', 11,
            ['Sacrifice_P'],
            1),
        ('Region_Zone0_Sacrifice_C', 12,
            ['Sacrifice_P'],
            1),
        ('Region_Zone1_Outskirts_A', 13,
            ['Outskirts_P'],
            0),
        ('Region_Zone1_Outskirts_B', 14,
            ['Outskirts_P'],
            0),
        ('Region_Zone1_City_A', 15,
            ['City_P', 'CreatureSlaughter_P', 'Desolate_P', 'Mine_P', 'Outskirts_P', 'Prison_P', 'Sanctuary3_P', 'Towers_P'],
            0),
        ('Region_Zone1_City_B', 16,
            ['CityVault_P', 'City_P', 'Outskirts_P', 'Sanctuary3_P'],
            0),
        ('Region_Zone1_City_C', 17,
            ['City_P', 'Outskirts_P'],
            0),
        ('Region_Zone1_Monastery_A', 18,
            ['CityVault_P', 'Monastery_P'],
            1),
        ('Region_Zone1_Monastery_Beans', 19,
            ['Monastery_P'],
            0),
        ('Region_Zone1_Monastery_CaptTraunt', 20,
            ['Monastery_P'],
            0),
        ('Region_Zone1_OrbitalPlatform_A', 21,
            ['OrbitalPlatform_P', 'TechSlaughter_P'],
            0),
        ('Region_Zone1_OrbitalPlatform_B', 22,
            ['OrbitalPlatform_P'],
            0),
        ('Region_Zone1_OrbitalPlatform_KatagawaSphere', 23,
            ['OrbitalPlatform_P'],
            0),
        ('Region_Zone1_Towers_A', 24,
            ['AtlasHQ_P', 'Towers_P'],
            0),
        ('Region_Zone1_Towers_B', 25,
            ['Towers_P'],
            0),
        ('Region_Zone1_Towers_KillaVolt', 26,
            ['Towers_P'],
            0),
        ('Region_Zone1_AtlasHQ', 27,
            ['AtlasHQ_P', 'CityVault_P'],
            0),
        ('Region_Zone1_AtlasHQ_B', 28,
            ['AtlasHQ_P'],
            0),
        ('Region_Zone1_AtlasHQ_KatagawaJr', 29,
            ['AtlasHQ_P'],
            0),
        ('Region_Zone1_City_Vault', 30,
            ['CityVault_P', 'Sanctuary3_P'],
            0),
        ('Region_Zone1_CityBoss', 31,
            ['CityBoss_P'],
            0),
        ('Region_Zone2_Wetlands_A', 32,
            ['Desert_P', 'MarshFields_P', 'Prison_P', 'Wetlands_P'],
            0),
        ('Region_Zone2_Wetlands_B', 33,
            ['WetlandsVault_P', 'Wetlands_P'],
            1),
        ('Region_Zone2_Wetlands_C', 34,
            ['Wetlands_P'],
            1),
        ('Region_Zone2_Prison_A', 35,
            ['Prison_P'],
            1),
        ('Region_Zone2_Prison_B', 36,
            ['Prison_P'],
            0),
        ('Region_Zone2_Prison_C', 37,
            ['Prison_P'],
            0),
        ('Region_Zone2_Prison_Warden', 38,
            ['Prison_P'],
            0),
        ('Region_Zone2_Mansion_A', 39,
            ['AtlasHQ_P', 'Mansion_P'],
            0),
        ('Region_Zone2_Mansion_B', 40,
            ['Mansion_P'],
            0),
        ('Region_Zone2_Mansion_Aurelia', 41,
            ['Mansion_P'],
            0),
        ('Region_Zone2_Watership', 42,
            ['Sanctuary3_P', 'Watership_P'],
            0),
        ('Region_Zone2_Watership-GeneVIV', 43,
            ['Watership_P'],
            0),
        ('Region_Zone2_MarshFields_A', 44,
            ['Mansion_P', 'MarshFields_P', 'WetlandsVault_P', 'Wetlands_P'],
            0),
        ('Region_Zone2_MarshFields_B', 45,
            ['MarshFields_P'],
            0),
        ('Region_Zone2_WetlandsVault', 46,
            ['CityVault_P', 'WetlandsBoss_P', 'WetlandsVault_P'],
            0),
        ('Region_Zone2_WetlandsBoss', 47,
            ['WetlandsBoss_P'],
            0),
        ('Region_Zone3_Desert_A', 48,
            ['CreatureSlaughter_P', 'Desert_P'],
            0),
        ('Region_Zone3_Desert_B', 49,
            ['Desert_P'],
            1),
        ('Region_Zone3_Desert_C', 50,
            ['Desert_P'],
            1),
        ('Region_Zone3_Mine', 51,
            ['Convoy_P', 'Mine_P'],
            0),
        ('Region_Zone3_Motorcade', 52,
            ['MotorcadeFestival_P', 'MotorcadeInterior_P', 'Motorcade_P', 'Prison_P'],
            0),
        ('Region_Zone3_MotorcadeFest', 53,
            ['MotorcadeFestival_P', 'Prison_P'],
            0),
        ('Region_Zone3_Motorcade_Interior', 54,
            ['MotorcadeInterior_P'],
            0),
        ('Region_Zone3_DesertVault', 55,
            ['CityBoss_P', 'DesertBoss_P', 'DesertVault_P', 'Desert_P', 'Monastery_P', 'Sanctuary3_P'],
            0),
        ('Region_Zone3_DesertBoss', 56,
            ['DesertBoss_P'],
            0),
        ('Region_Zone4_Desolate_A', 57,
            ['Beach_P', 'Crypt_P', 'Desolate_P', 'Mine_P', 'Motorcade_P'],
            0),
        ('Region_Zone4_Desolate_B', 58,
            ['Desolate_P'],
            0),
        ('Region_Zone4_Desolate_C', 59,
            ['Desolate_P'],
            0),
        ('Region_Zone4_Desolate_Traunt', 60,
            ['Desolate_P'],
            0),
        ('Region_Zone4_Beach', 61,
            ['Beach_P', 'MotorcadeFestival_P'],
            0),
        ('Region_Zone4_Desolate_Crypt', 62,
            ['Crypt_P'],
            0),
        # Mission override count only exists because of the GBX hotfix SparkLevelPatchEntry119
        ('Region_Zone0_FinalBoss', 63,
            ['CityBoss_P', 'Crypt_P', 'DesertBoss_P', 'FinalBoss_P', 'Sanctuary3_P', 'WetlandsBoss_P'],
            1),
        ]:

    for level in levels:

        mod.reg_hotfix(Mod.LEVEL, level,
                '/Game/GameData/Regions/RegionManagerData',
                'PlayThroughs.PlayThroughs[0].Regions.Regions[{}].MaxGameStage'.format(r_idx),
                100)

        for m_idx in range(num_missions):
            mod.reg_hotfix(Mod.LEVEL, level,
                    '/Game/GameData/Regions/RegionManagerData',
                    'PlayThroughs.PlayThroughs[0].Regions.Regions[{}].MissionOverrides.MissionOverrides[{}].MaxGameStage'.format(r_idx, m_idx),
                    100)

mod.close()