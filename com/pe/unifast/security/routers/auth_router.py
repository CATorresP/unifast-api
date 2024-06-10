@router.get("/account/")
async def get_my_account(current_user: Annotated[dict, Depends(get_token_info)]):
    return current_user



@router.get("/item/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}