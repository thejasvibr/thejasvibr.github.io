def amazefunction(amaze_type, **kwargs):
    '''Creates an amazing thing. 
    
    Parameters
    ----------
    amaze_type : str
        The type of amazing object to be created.
        Possible value ['unicorn', 'rakshasa', 'wolpertinger']
    
    Returns
    -------
    amazingness : dictionary
        The amazingness dictionary has keys
        'height', 'weight', 'powers' and other  optional
        descriptive features controlled by optional 
        arguments.

    See Also
    --------
    make_amazing_object
    check_amaze_type
    '''
    # check appropriate amazingness
    check_amaze_type(amaze_type, **kwargs)

    # make amazing object
    amazingness = make_amazing_object(amazetype, **kwargs)
    return amazingness

help(amazefunction)
