from __future__ import annotations

from random import sample, choices, randint
from typing import TYPE_CHECKING

from scripts.cat.enums import CatRank
from scripts.cat.factories.new_cat_factory import NewCatFactory
from scripts.cat.factories.test_cat_factory import TestCatFactory
from scripts.cat.pelts import Pelt

if TYPE_CHECKING:
    from scripts.cat.cats import Cat


def create_example_cats(majority_rank: CatRank, rank_weights: dict) -> list["Cat"]:
    majority_rank_cats = sample(range(12), 3)

    chosen_cats = []
    for cat_index in range(12):
        if cat_index in majority_rank_cats:
            new_cat = NewCatFactory.create_cat(rank=majority_rank)
        else:
            random_rank = choices(
                list(rank_weights.keys()), list(rank_weights.values())
            )[0]
            new_cat = NewCatFactory.create_cat(rank=random_rank)

        if new_cat.moons >= 140:
            new_cat.moons = randint(120, 140)
        chosen_cats.append(new_cat)

    return chosen_cats


def create_option_preview_cat(scar: str = None, acc: str = None):
    """
    Creates a cat with the specified scar and/or accessory.
    :param scar: Desired scar (only one)
    :param acc: Desired accessory (only one)
    """
    new_cat = TestCatFactory.create_cat(
        moons=60,
        loading_cat=True,
        pelt=Pelt(
            name="SingleColour",
            colour="WHITE",
            length="medium",
            texture="fluffy",
            size="short",
            build="strong",
            physical_trait_1=cat["physical_trait_1"] if "physical_trait_1" in cat else None,
            physical_trait_2=cat["physical_trait_2"] if "physical_trait_2" in cat else None,
            physical_trait_3=cat["physical_trait_3"] if "physical_trait_3" in cat else None,
            physical_trait_4=cat["physical_trait_4"] if "physical_trait_4" in cat else None,
            physical_trait_hidden=cat["physical_trait_hidden"] if "physical_trait_hidden" in cat else None,
            physical_trait_hidden_2=cat["physical_trait_hidden_2"] if "physical_trait_hidden_2" in cat else None,
            physical_trait_hidden_3=cat["physical_trait_hidden_3"] if "physical_trait_hidden_3" in cat else None,
            physical_trait_hidden_4=cat["physical_trait_hidden_4"] if "physical_trait_hidden_4" in cat else None,
            eye_color="SAGE",
            reverse=False,
            white_patches=[white_patches] if white_patches else [],
            vitiligo=None,
            points=None,
            tortie_marking=None,
            tortie_base=None,
            tortie_pattern=None,
            tortie_colour=None,
            tint="gray",
            skin="BLUE",
            scars=[scar] if scar else [],
            adult_sprite="8",
            accessory=[acc] if acc else [],
        ),
    )

    return new_cat
