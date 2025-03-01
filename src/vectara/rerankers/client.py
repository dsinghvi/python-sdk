# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..core.pagination import SyncPager
from ..types.reranker import Reranker
from ..types.list_rerankers_response import ListRerankersResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.forbidden_error import ForbiddenError
from ..types.error import Error
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper
from ..core.pagination import AsyncPager


class RerankersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        filter: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Reranker]:
        """
        Rerankers are used to improve the ranking (ordering) of search results.

        Parameters
        ----------
        filter : typing.Optional[str]
            A regular expression against reranker names and descriptions.

        limit : typing.Optional[int]
            The maximum number of rerankers to return in the list.

        page_key : typing.Optional[str]
            Used to the retrieve the next page of rerankers after the limit has been reached.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Reranker]
            List of rerankers.

        Examples
        --------
        from vectara import Vectara

        client = Vectara(
            api_key="YOUR_API_KEY",
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        response = client.rerankers.list(
            filter="vectara.*",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/rerankers",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "filter": filter,
                "limit": limit,
                "page_key": page_key,
            },
            headers={
                "Request-Timeout": str(request_timeout) if request_timeout is not None else None,
                "Request-Timeout-Millis": str(request_timeout_millis) if request_timeout_millis is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListRerankersResponse,
                    parse_obj_as(
                        type_=ListRerankersResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = False
                _get_next = None
                if _parsed_response.metadata is not None:
                    _parsed_next = _parsed_response.metadata.page_key
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        filter=filter,
                        limit=limit,
                        page_key=_parsed_next,
                        request_timeout=request_timeout,
                        request_timeout_millis=request_timeout_millis,
                        request_options=request_options,
                    )
                _items = _parsed_response.rerankers
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRerankersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        filter: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Reranker]:
        """
        Rerankers are used to improve the ranking (ordering) of search results.

        Parameters
        ----------
        filter : typing.Optional[str]
            A regular expression against reranker names and descriptions.

        limit : typing.Optional[int]
            The maximum number of rerankers to return in the list.

        page_key : typing.Optional[str]
            Used to the retrieve the next page of rerankers after the limit has been reached.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Reranker]
            List of rerankers.

        Examples
        --------
        import asyncio

        from vectara import AsyncVectara

        client = AsyncVectara(
            api_key="YOUR_API_KEY",
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            response = await client.rerankers.list(
                filter="vectara.*",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/rerankers",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "filter": filter,
                "limit": limit,
                "page_key": page_key,
            },
            headers={
                "Request-Timeout": str(request_timeout) if request_timeout is not None else None,
                "Request-Timeout-Millis": str(request_timeout_millis) if request_timeout_millis is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListRerankersResponse,
                    parse_obj_as(
                        type_=ListRerankersResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = False
                _get_next = None
                if _parsed_response.metadata is not None:
                    _parsed_next = _parsed_response.metadata.page_key
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        filter=filter,
                        limit=limit,
                        page_key=_parsed_next,
                        request_timeout=request_timeout,
                        request_timeout_millis=request_timeout_millis,
                        request_options=request_options,
                    )
                _items = _parsed_response.rerankers
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
